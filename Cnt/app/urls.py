from . import views
from django.urls import path,  include

app_name = 'app'

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('accordion', views.accordion, name='accordion'),
    path('alerts', views.alerts, name='alerts'),
    path('avatar', views.avatar, name='avatar'),
    path('background', views.background, name='background'),
    path('badge', views.badge, name='badge'),
    path('blog-details', views.blog_details, name='blog-details'),
    path('blog-edit', views.blog_edit, name='blog-edit'),
    path('blog', views.blog, name='blog'),
    path('border', views.border, name='border'),
    path('breadcrumbs', views.breadcrumbs, name='breadcrumbs'),
    path('buttons', views.buttons, name='buttons'),
    path('calendar2', views.calendar2, name='calendar2'),
    path('cards', views.cards, name='cards'),
    path('carousel', views.carousel, name='carousel'),
    path('cart', views.cart, name='cart'),
    path('chart-chartjs', views.chart_chartjs, name='chart-chartjs'),
    path('chart-echart', views.chart_echart, name='chart-echart'),
    path('chart-flot', views.chart_flot, name='chart-flot'),
    path('chart-morris', views.chart_morris, name='chart-morris'),
    path('chart-nvd3', views.chart_nvd3, name='chart-nvd3'),
    path('chat', views.chat, name='chat'),
    path('checkout', views.checkout, name='checkout'),
    path('client-create', views.client_create, name='client-create'),
    path('clients', views.clients, name='clients'),
    path('colors', views.colors, name='colors'),
    path('construction', views.construction, name='construction'),
    path('counters', views.counters, name='counters'),
    path('datatable', views.datatable, name='datatable'),
    path('display', views.display, name='display'),
    path('dropdown', views.dropdown, name='dropdown'),
    path('empty', views.empty, name='empty'),
    path('error404', views.error404, name='error404'),
    path('error500', views.error500, name='error500'),
    path('error501', views.error501, name='error501'),
    path('faq', views.faq, name='faq'),
    path('file-attachments', views.file_attachments, name='file-attachments'),
    path('file-manager-1', views.file_manager_1, name='file-manager-1'),
    path('file-manager-2', views.file_manager_2, name='file-manager-2'),
    path('file-manager', views.file_manager, name='file-manager'),
    path('flex', views.flex, name='flex'),
    path('footers', views.footers, name='footers'),
    path('forgot-password', views.forgot_password, name='forgot-password'),
    path('form-advanced', views.form_advanced, name='form-advanced'),
    path('form-editable', views.form_editable, name='form-editable'),
    path('form-elements', views.form_elements, name='form-elements'),
    path('form-layouts', views.form_layouts, name='form-layouts'),
    path('form-validation', views.form_validation, name='form-validation'),
    path('form-wizard', views.form_wizard, name='form-wizard'),
    path('gallery', views.gallery, name='gallery'),
    path('height', views.height, name='height'),
    path('icons', views.icons, name='icons'),
    path('icons2', views.icons2, name='icons2'),
    path('icons3', views.icons3, name='icons3'),
    path('icons4', views.icons4, name='icons4'),
    path('icons5', views.icons5, name='icons5'),
    path('icons6', views.icons6, name='icons6'),
    path('icons7', views.icons7, name='icons7'),
    path('icons8', views.icons8, name='icons8'),
    path('icons9', views.icons9, name='icons9'),
    path('icons10', views.icons10, name='icons10'),
    path('index', views.index, name='index'),
    path('invoice-create', views.invoice_create, name='invoice-create'),
    path('invoice-details', views.invoice_details, name='invoice-details'),
    path('invoice-edit', views.invoice_edit, name='invoice-edit'),
    path('invoice-list', views.invoice_list, name='invoice-list'),
    path('invoice-timelog', views.invoice_timelog, name='invoice-timelog'),
    path('landing', views.landing, name='landing'),
    path('loaders', views.loaders, name='loaders'),
    path('lockscreen', views.lockscreen, name='lockscreen'),
    path('login2', views.login, name='login2'),
    path('mail-compose', views.mail_compose, name='mail-compose'),
    path('mail-inbox', views.mail_inbox, name='mail-inbox'),
    path('mail-read', views.mail_read, name='mail-read'),
    path('mail-settings', views.mail_settings, name='mail-settings'),
    path('maps', views.maps, name='maps'),
    path('maps1', views.maps1, name='maps1'),
    path('maps2', views.maps2, name='maps2'),
    path('margin', views.margin, name='margin'),
    path('mediaobject', views.mediaobject, name='mediaobject'),
    path('modal', views.modal, name='modal'),
    path('navigation', views.navigation, name='navigation'),
    path('notify', views.notify, name='notify'),
    path('offcanvas', views.offcanvas, name='offcanvas'),
    path('opacity', views.opacity, name='opacity'),
    path('padding', views.padding, name='padding'),
    path('pagination', views.pagination, name='pagination'),
    path('panels', views.panels, name='panels'),
    path('position', views.position, name='position'),
    path('pricing', views.pricing, name='pricing'),
    path('product-details', views.product_details, name='product-details'),
    path('products', views.products, name='products'),
    path('profile', views.profile, name='profile'),
    path('progress', views.progress, name='progress'),
    path('project-details', views.project_details, name='project-details'),
    path('project-edit', views.project_edit, name='project-edit'),
    path('project-new', views.project_new, name='project-new'),
    path('projects-list', views.projects_list, name='projects-list'),
    path('projects', views.projects, name='projects'),
    path('rangeslider', views.rangeslider, name='rangeslider'),
    path('rating', views.rating, name='rating'),
    path('register', views.register, name='register'),
    path('scroll', views.scroll, name='scroll'),
    path('services', views.services, name='services'),
    path('settings', views.settings, name='settings'),
    path('sweetalert', views.sweetalert, name='sweetalert'),
    path('switcherpage', views.switcherpage, name='switcherpage'),
    path('table-editable', views.table_editable, name='table-editable'),
    path('tables', views.tables, name='tables'),
    path('tabs', views.tabs, name='tabs'),
    path('tags', views.tags, name='tags'),
    path('task-create', views.task_create, name='task-create'),
    path('task-edit', views.task_edit, name='task-edit'),
    path('tasks-list', views.tasks_list, name='tasks-list'),
    path('terms', views.terms, name='terms'),
    path('thumbnails', views.thumbnails, name='thumbnails'),
    path('ticket-details', views.ticket_details, name='ticket-details'),
    path('timeline', views.timeline, name='timeline'),
    path('tooltipandpopover', views.tooltipandpopover, name='tooltipandpopover'),
    path('treeview', views.treeview, name='treeview'),
    path('typography', views.typography, name='typography'),
    path('users-list', views.users_list, name='users-list'),
    path('width', views.width, name='width'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('wysiwyag', views.wysiwyag, name='wysiwyag'),
]