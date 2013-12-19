from django.conf.urls import patterns, url
# # from blog.rss import RssFeed

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^login/$', 'blog.views.login', name='login'),
    url(r'^sign_up/$', 'blog.views.sign_up', name='sign_up'),
    url(r'^sign_up_done/$', 'blog.views.sign_up_done', name='sign_up_done'),
    url(r'^login_done/$', 'blog.views.login_done', name='login_done'),
    # url(r'^blog_pg/$', 'blog.vi	ews.blog_pg', name='blog_pg'),
    url(r'^blog_list$', 'blog.views.blog_list', name='blog_list'),
    url(r'^logout_first/$','blog.views.logout_first', name='logout_first'),
    url(r'^logout/$','blog.views.logout',name='logout'),
    url(r'^logout_done/$','blog.views.logout_done',name='logout_done'),
    url(r'^add_blog/$','blog.views.add_blog',name='add_blog'),
    url(r'^add_blog_done/$','blog.views.add_blog_done',name='add_blog_done'),
    url(r'^login_first/$','blog.views.login_first',name='login_first'),
    url(r'^blog_pg/(?P<blog_id>\d+)/(?P<page_id>\d+)/$','blog.views.blog_pg',name='blog_pg'),
    url(r'^post_pg/$','blog.views.post_pg',name='post_pg'),
    url(r'^tag/(?P<tag_id>\d+)/(?P<page_id>\d+)/$','blog.views.tag',name='tag'),
    url(r'^add_post/(?P<blog_id>\d+)/$','blog.views.add_post',name='add_post'),
    url(r'^add_post_done/(?P<blog_id>\d+)/$','blog.views.add_post_done',name='add_post_done'),

)