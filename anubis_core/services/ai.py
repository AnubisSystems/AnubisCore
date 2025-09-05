import base64
from io import BytesIO
import uuid

from anubis_core.models.ai_manager import AIRecipeList
from anubis_core.ports.ai_service_manager import IAIAnalizeServicePort, IAIServicesManagerPort, IAIServicesPort
from anubis_core.ports.cdn_manager import ICdnManagerPort
from anubis_core.ports.db import IVectorSearchPort
from anubis_core.ports.tools import ITemplateEnviromentPort
from anubis_core.ports.web import IWebSearchPort


class IAImageRecognitonClasify(IAIAnalizeServicePort):

    def __init__(self, 
                  ia_adapter: IAIServicesManagerPort,
                  prompt_identify: str, 
                  prompt_clasify: str,
                  model_identify: str = "gpt-4o", 
                  model_clasify: str = "gpt-3.5-turbo",
                  debug = False
                 ):
        
        self.ia_adapter = ia_adapter
        self.prompt_identify = prompt_identify
        self.prompt_clasify = prompt_clasify
        self.model_identify = model_identify
        self.model_clasify = model_clasify
        self.debug = debug

        pass

    def process(self, image_base64: str) -> tuple[any,AIRecipeList]:
        return self.process_to_json(image_base64)
    
    @property    
    def name(self) -> str:
        return f"{self.model_identify} + {self.model_clasify}"
        

    def process_to_json(self, image_base64: str) -> tuple[any,AIRecipeList]:
        costs : AIRecipeList = AIRecipeList()
        response_ia , cost = self.ia_adapter.get_chat_completion(self.model_identify,self.prompt_identify,image_base64=image_base64)        
        costs.recipes_ai.append(cost)
        if self.debug : 
            print(response_ia)

        response_json , cost = self.ia_adapter.get_chat_completion_json(self.model_clasify, response_ia, context=self.prompt_clasify)        
        costs.recipes_ai.append(cost)
        
        if self.debug : 
            print(response_json)
            print(costs.total_price())
        
        return response_json , costs
    
    def process_to_text_json(self, image_base64: str) -> tuple[any,AIRecipeList]:
        return self.process_to_json(image_base64)
    
    def process_to_text(self, image_base64):        
        raise NotImplementedError("Esta función aún no está implementada.")

    
class IAImageRecogniton(IAIAnalizeServicePort):
    def __init__(self, 
                  ia_adapter: IAIServicesManagerPort,
                  prompt_identify: str,             
                  model_identify: str = "gpt-4o",             
                  debug = False
                 ):
        
        self.ia_adapter = ia_adapter
        self.prompt_identify = prompt_identify        
        self.model_identify = model_identify        
        self.debug = debug

    def process(self, image_base64: str) -> tuple[any,AIRecipeList]:
        return self.process_to_text_json(image_base64)
    
    @property    
    def name(self) -> str:
        return f"{self.model_identify}"

    def process_to_text(self, image_base64: str) -> tuple[any,AIRecipeList]:
        costs : AIRecipeList = AIRecipeList()
        response_ia , cost = self.ia_adapter.get_chat_completion(self.model_identify,prompt=self.prompt_identify,image_base64=image_base64)     
        costs.recipes_ai.append(cost)
        
        if self.debug : 
            print(response_ia)
            print(costs.total_price())        

        return response_ia , costs
        


    def process_to_text_prompt(self, image_base64: str,prompt:str) -> tuple[any,AIRecipeList]:
        costs : AIRecipeList = AIRecipeList()
        response_ia , cost = self.ia_adapter.get_chat_completion(self.model_identify,prompt=prompt,image_base64=image_base64,context=self.prompt_identify)     
        costs.recipes_ai.append(cost)
        
        if self.debug : 
            print(response_ia)
            print(costs.total_price())        

        return response_ia , costs       

    def process_to_text_json(self, image_base64: str) -> tuple[any,AIRecipeList]:
        costs : AIRecipeList = AIRecipeList()
        response_ia , cost = self.ia_adapter.get_chat_completion_json(self.model_identify,prompt=self.prompt_identify,image_base64=image_base64)
        costs.recipes_ai.append(cost)
        
        if self.debug : 
            print(response_ia)
            print(costs.total_price())        

        return response_ia , costs      
           
    def process_to_text_content_json(self, image_base64: str, context) -> tuple[any,AIRecipeList]:
        costs : AIRecipeList = AIRecipeList()
        response_ia , cost = self.ia_adapter.get_chat_completion_json(self.model_identify,prompt=self.prompt_identify,image_base64=image_base64,context=context)
        costs.recipes_ai.append(cost)
        
        if self.debug : 
            print(response_ia)
            print(costs.total_price())        

        return response_ia , costs      
 

    def process_to_text_prompt_json(self, image_base64, prompt) -> tuple[any,AIRecipeList]:
        costs : AIRecipeList = AIRecipeList()
        response_ia , cost = self.ia_adapter.get_chat_completion_json( self.model_identify, prompt, image_base64=image_base64,context=self.prompt_identify)
        costs.recipes_ai.append(cost)
        
        if self.debug : 
            print(response_ia)
            print(costs.total_price())        

        return response_ia , costs      
         

class   AIAnalizeServicesImageRecognitonClasifyService(IAIAnalizeServicePort):

   

    def __init__(self,
                 cdn_adapter: ICdnManagerPort = None,
                 template_adapter: ITemplateEnviromentPort = None,
                 vector_db: IVectorSearchPort = None) :    
        self.cdn_adapter = cdn_adapter    
        self.template_adapter = template_adapter
        self.vector_db = vector_db

        import unicodedata
        import numpy as np
        import seaborn as sns
        import matplotlib.pyplot as plt
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.metrics import jaccard_score
        pass

    
    def process(self, 
                ai_services : list[IAIServicesPort], 
                images_base64 : list[str],
                name: str,
                solutions: dict = None

                ) -> dict:
        id_ = str(uuid.uuid4())
        output = {
            "name" : name,
            "id": id_,
            "filename": f"{id_}.html",
            "elements":[],
            "totals" : {},            
        }
        i = 0
        for image_base64 in images_base64:
            id_documento = str(uuid.uuid4())
            if self.cdn_adapter:
                id_imagen = f"{id_documento}.jpg"
                url_image = self.cdn_adapter.send_file(id_imagen,image_base64,"Enviando imagen")
            else:
                url_image = image_base64

            item = {"img": url_image,
                    "responses_ai": {}
                    }
            
            responses_for_compare = []
            if solutions:
                responses_for_compare.append({"response":solutions[i],"name":"la metralleta"})

                item["responses_ai"]["la metralleta"] = {
                            "response_ai": solutions[i],
                            #"cost_ai": cost_ai
                            }
            for ai_service in ai_services:
                try:                     
                    response_ai, cost_ai = ai_service.process(image_base64 )                
                    responses_for_compare.append({"response":response_ai,"name":ai_service.name})
                    item["responses_ai"][ai_service.name] = {
                        "response_ai": response_ai,
                        #"cost_ai": cost_ai
                        }
                    if ai_service.name in output["totals"].keys():
                        output["totals"][ai_service.name]["price"] += cost_ai.total_price()
                        output["totals"][ai_service.name]["tokens"] += cost_ai.total_tokens()
                    else: 
                        output["totals"][ai_service.name] = {}
                        output["totals"][ai_service.name] = {}
                        output["totals"][ai_service.name]["price"] = cost_ai.total_price()
                        output["totals"][ai_service.name]["tokens"] = cost_ai.total_tokens()
                except Exception as ex:
                    item["responses_ai"][ai_service.name] = {"nombre": "ERROR EN AI" , "exception" : ex} 
            
            image_compare = self.compare(responses_for_compare)
            filename_image_compare = f"compare-{id_imagen}.png" 
            if self.cdn_adapter and self.template_adapter:
                url_image_compare = self.cdn_adapter.send_file(filename_image_compare,image_compare,f"Enviando comparativa AIS - {filename_image_compare}")
                item["url_image_compare"] = url_image_compare
            
            output["elements"].append(item)

            if self.vector_db:
                embebing = self.vector_db.create_embedding(image_base64)
                self.vector_db.index_document(id_documento,embebing,item["responses_ai"])
            
            i += 1


        if self.cdn_adapter and self.template_adapter:
            id_html = f"AIS-{id_}.html"            
            file_content = self.template_adapter.render("AIAnalizeServicesImageRecognitonClasifyService.html",data=output)                
            url_image = self.cdn_adapter.send_file(id_html,base64.b64encode(file_content.encode('utf-8')).decode('utf-8'),f"Enviando informe AIS - {id_html}")
            return {"url":url_image}
        else:
            return output
        
    def compare(self, results, solutions: dict = None):
        original = {
            "Nombre": "hola",
            "Descripcion": "self.comparar_texto",            
            "Precio": 2,
            "Año": 1964,            
            # puedes añadir más campos y estrategias aquí
        }

        # Diccionario dinámico de comparadores
        estrategias = {
            "Nombre": self.comparar_texto,                       
            "Precio": self.comparar_exactos,
            "Descripcion": self.comparar_texto, 
            "Año": self.comparar_anios,            
            # puedes añadir más campos y estrategias aquí
        }

        


        models_ia = [d["name"][:6] + "..." if len(d["name"]) > 6 else d["name"] for d in results]
        datos = [d["response"] for d in results]

        if solutions:
            datos = [solutions] + datos

        campos_a_comparar = [k for k in original.keys() if k != "etiqueta" and k in estrategias]
        
        # Calcular el número de filas necesarias (2 gráficos por fila)
        num_campos = len(campos_a_comparar)
        num_filas = (num_campos + 1) // 2  # Redondeo hacia arriba
        
        # Crear figura con disposición de 2 columnas
        fig, axes = plt.subplots(num_filas, 2, figsize=(12, 5 * num_filas))
        
        # Si solo hay un gráfico, axes no será un array 2D
        if num_campos == 1:
            axes = np.array([[axes]])
        elif num_filas == 1:
            axes = axes.reshape(1, -1)
        
        # Aplanar el array de axes para facilitar el acceso
        axes_flat = axes.flatten()
        
        # Procesar cada campo dinámicamente
        for idx, campo in enumerate(campos_a_comparar):
            valores = []
            for d in datos:
                valores.append(d.get(campo, ""))
            # valores = [d.get(campo, "") ]
            comparador = estrategias[campo]
            matriz, cmap = comparador(valores)
            sns.heatmap(matriz, annot=True, cmap=cmap, xticklabels=models_ia, yticklabels=models_ia, ax=axes_flat[idx])
            axes_flat[idx].set_title(f"Similitud: {campo}")
        
        # Ocultar ejes vacíos si el número de campos es impar
        for idx in range(num_campos, num_filas * 2):
            axes_flat[idx].axis('off')
        
        plt.tight_layout()
        
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        plt.close()
        # Obtiene los bytes del buffer y codifícalos en base64
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return image_base64


        # Normalización de texto
    def normalizar(self,texto):
        if not isinstance(texto, str):
            texto = str(texto)
        texto = texto.lower()
        texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
        return texto

    # Comparadores por tipo de campo
    def comparar_texto(self,valores):
        valores_norm = [self.normalizar(v) for v in valores]
        vectorizer = CountVectorizer(binary=True).fit_transform(valores_norm)
        sim_matrix = np.zeros((len(valores), len(valores)))
        for i in range(len(valores)):
            for j in range(len(valores)):
                v1 = vectorizer[i].toarray()[0]
                v2 = vectorizer[j].toarray()[0]
                sim_matrix[i, j] = jaccard_score(v1, v2)
        return sim_matrix, "YlGnBu"

    def comparar_exactos(self,valores):
        sim_matrix = np.zeros((len(valores), len(valores)))
        for i in range(len(valores)):
            for j in range(len(valores)):
                sim_matrix[i, j] = 1.0 if valores[i] == valores[j] else 0.0
        return sim_matrix, "YlOrBr"

    def comparar_anios(self,valores):
        valores = [str(v).strip() for v in valores]
        sim_matrix = np.zeros((len(valores), len(valores)))
        for i in range(len(valores)):
            for j in range(len(valores)):
                if valores[i].isdigit() and valores[j].isdigit():
                    sim_matrix[i, j] = 1.0 if valores[i] == valores[j] else 0.0
                else:
                    sim_matrix[i, j] = 0.0
        return sim_matrix, "YlGn"
    
class   AIAnalizeServicesImageRecognitonSearchSimilarsService(IAIAnalizeServicePort):

    def __init__(self, 
                  ia_adapter: IAIServicesManagerPort,
                  prompt_identify: str, 
                  prompt_clasify: str,
                  search_sites: dict[str,IWebSearchPort], 
                  model_identify: str = "gpt-4o", 
                  model_clasify: str = "gpt-3.5-turbo",                  
                  debug = False
                 ):
        
        self.ia_adapter = ia_adapter
        self.prompt_identify = prompt_identify
        self.prompt_clasify = prompt_clasify
        self.model_identify = model_identify
        self.model_clasify = model_clasify        
        self.search_sites = search_sites
        self.debug = debug

        pass

    def process(self, image_base64: str) -> tuple[any,AIRecipeList]:
        return self.process_to_json(image_base64)
    
    @property    
    def name(self) -> str:
        return f"{self.model_identify} + {self.model_clasify}"
        

    @property    
    def sites(self) -> dict:
        return [
            {"site":"leroymerlin.es" , "includes":"www.leroymerlin.es/productos/*", "excludes":"leroymerlin.es/productos/*/*"}
        ]

    def process_to_text_json(self, image_base64: str) -> tuple[any,AIRecipeList]:
        return self.process_to_json(image_base64)

    def process_to_json(self, image_base64: str) -> tuple[any,AIRecipeList]:
        costs : AIRecipeList = AIRecipeList()
        response_identify , cost = self.ia_adapter.get_chat_completion_json(self.model_identify,self.prompt_identify,image_base64=image_base64)        
        costs.recipes_ai.append(cost)
        if self.debug : 
            print(response_identify)

        print(response_identify)
        """PROCESAMOS CADA PRODUCTO ENCONTRADO.
        """
        for item in response_identify["materiales_encontrados"]:
            item["urls_validated"] = ""
            for key in self.search_sites.keys():
                if key in item["url"]:
                    item["urls_validated"] = self.search_sites[key]().search(item["nombre"],rows=1,id_search="b06403cd26b3e4f93")
                    break
            print (item["urls_validated"])    
        
        if self.debug :             
            print(costs.total_price())
        
        return response_identify , costs
    

