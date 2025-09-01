# 🛍️ Plataformas eCommerce con API para Publicar Productos

## Generalistas

| Plataforma              | Tipo             | Nicho / Descripción                                         | API Disponible |
|------------------------|------------------|-------------------------------------------------------------|----------------|
| **Amazon Seller**      | SaaS             | Marketplace global para todo tipo de productos.             | ✅ [API Docs](https://developer.amazonservices.com) |
| **PrestaShop**         | On-premise/SaaS  | CMS open-source muy usado en Europa.                        | ✅ [API Docs](https://devdocs.prestashop-project.org) |
| **Shopify**            | SaaS             | Plataforma moderna con API robusta.                         | ✅ [API Docs](https://shopify.dev/docs) |
| **WooCommerce**        | On-premise       | Plugin de WordPress para tiendas online.                    | ✅ [API Docs](https://woocommerce.github.io/woocommerce-rest-api-docs) |
| **Magento (Adobe)**    | On-premise/SaaS  | Potente y escalable, ideal para grandes catálogos.          | ✅ [API Docs](https://developer.adobe.com/commerce/webapi/rest/) |
| **BigCommerce**        | SaaS             | Enfocado en escalabilidad y multicanal.                     | ✅ [API Docs](https://developer.bigcommerce.com) |
| **VTEX**               | SaaS             | Plataforma enterprise con enfoque headless.                 | ✅ [API Docs](https://developers.vtex.com) |
| **Tiendanube**         | SaaS             | Líder en LATAM, fácil de usar.                              | ✅ [API Docs](https://developers.tiendanube.com) |
| **Ecwid**              | SaaS             | Se integra fácilmente en webs existentes.                   | ✅ [API Docs](https://api-docs.ecwid.com) |
| **LogiCommerce**       | SaaS/On-premise  | Modular, orientado a B2B y B2C.                             | ✅ [API Docs](https://docs.logicommerce.com) |

---

## 🎵 Plataformas Especializadas en Música

| Plataforma              | Tipo             | Nicho / Descripción                                         | API Disponible |
|------------------------|------------------|-------------------------------------------------------------|----------------|
| **Discogs Marketplace**| SaaS             | Venta de vinilos, CDs, cassettes y música coleccionable.   | ✅ [API Docs](https://www.discogs.com/developers) |
| **Bandcamp**           | SaaS             | Venta directa de música por artistas independientes.        | ❌ No pública (solo para partners) |
| **Beatport**           | SaaS             | Música electrónica, DJs y productores.                      | ❌ No pública (uso interno y licenciado) |

---

## 🎬 Plataformas Especializadas en Cine y Coleccionismo

| Plataforma              | Tipo             | Nicho / Descripción                                         | API Disponible |
|------------------------|------------------|-------------------------------------------------------------|----------------|
| **eBay**               | SaaS             | Ideal para coleccionismo: películas, figuras, rarezas.      | ✅ [API Docs](https://developer.ebay.com) |
| **Catawiki**           | SaaS             | Subastas de objetos únicos: arte, cine, música, etc.        | ❌ No pública (uso interno) |
| **FilmArt Gallery**    | SaaS             | Venta de pósters originales de películas clásicas.          | ❌ No disponible |
| **Heritage Auctions**  | SaaS             | Subastas de memorabilia, cómics, cine, música.              | ❌ No disponible |

---

## ✅ Recomendaciones

- Prioriza plataformas con **API RESTful bien documentadas** para facilitar el desarrollo de adaptadores.
- Para nichos cerrados como Bandcamp o Heritage, considera acuerdos de integración directa o alternativas con API pública como Discogs y eBay.
- Puedes usar una capa de normalización para unificar atributos como título, edición, formato, año, etc., especialmente útil en productos culturales.
