from anubis_core.features.blog.models import CorePost
from anubis_core.features.blog.ports import IPostAdapter

class BlogPostService():
    def __init__(self, post_adapter: IPostAdapter  ):

        self.post_adapter = post_adapter


    def push_post(self, post : CorePost) -> CorePost:
        return self.post_adapter.push_post(post)
        

    def pull_post(self, id_post:int ) -> CorePost:
        return self.post_adapter.pull_post(id_post)
        

    def search_posts(self, search_text :str) -> list[CorePost]:
        return self.post_adapter.search_posts(search_text=search_text)
        

