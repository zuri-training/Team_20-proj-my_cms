from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool


class Menu(CMSToolbar):
    [...]


toolbar_pool.register(Menu)
