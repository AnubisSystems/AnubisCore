from pydantic import BaseModel
from typing import List, Optional, Dict

class AIRecipe(BaseModel):
    
    id: str
    """_summary_
    """

    endpoint: str
    
    model: str   

    messages: list

    raw_response: dict

    tokens_in : int 

    tokens_out: int

    price_tokens_in: float 
    """Price per 1.000.000 tokens

    Returns:
        _type_: _description_
    """

    price_tokens_out: float

    time_delta: str

    def total_price(self) -> float:
        price_per_token_in:float = float(self.price_tokens_in / 1000000)
        price_per_token_out:float = (self.price_tokens_out / 1000000)        
        return float(self.tokens_in * price_per_token_in) + float(self.tokens_out * price_per_token_out) 
    
    def total_tokens(self) -> int:
        return self.tokens_in + self.tokens_out

class AIRecipeList(BaseModel):

    recipes_ai: list[AIRecipe] = []

    def total_price(self) -> float:
        output = 0
        for recipe in self.recipes_ai:
            output += recipe.total_price()

        return output
    
    def total_tokens(self) -> int:
        output = 0
        for recipe in self.recipes_ai:
            output += recipe.total_tokens()

        return output    