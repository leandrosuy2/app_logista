from django.urls import path, include
from . import views
from .views import listar_devedores, listar_titulos_por_devedor, adicionar_devedor, editar_devedor, excluir_devedor, realizar_acordo, listar_acordos, pagar_parcela, detalhar_parcela, consultar_cnpj_view, adicionar_usuario, listar_usuarios, editar_usuario, excluir_usuario, listar_grupos, editar_grupo, atualizar_permissao, gerar_contrato, anexar_contrato 
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.conf.urls import handler403, static
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


 
handler403 = 'core.views.permission_denied_view'



urlpatterns = [
    path('', views.home_redirect, name='home'),  # Rota para redirecionar para o dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    # Relatórios
    path('relatorios/honorarios/', views.relatorio_honorarios, name='relatorio_honorarios'),
    path('relatorios/honorarios/exportar/', views.relatorio_honorarios_exportar, name='relatorio_honorarios_exportar'),
    path('relatorios/honorarios/comprovante/<int:titulo_id>/', views.relatorio_honorarios_comprovante, name='relatorio_honorarios_comprovante'),
    path('lojista/followups/<int:devedor_id>/', views.followups_devedor_json, name='followups_devedor_json'),
    path('devedores/listar/', listar_devedores, name='devedores_listar'),
    path('agendamentos/cadastrar/', views.agendamentos_cadastrar, name='agendamentos_cadastrar'),       
    path('devedores/', views.listar_devedores, name='listar_devedores'),
    path('acordos/parcela/<int:parcela_id>/editar/',  views.parcela_editar,  name='editar_parcela'),
    path('acordos/parcela/<int:parcela_id>/excluir/', views.parcela_excluir, name='excluir_parcela'),
    path('devedores/adicionar/', views.adicionar_devedor, name='adicionar_devedor'),
    path('devedores/<int:id>/editar/', editar_devedor, name='editar_devedor'),
    path('devedores/<int:id>/excluir/', excluir_devedor, name='excluir_devedor'),
    path('devedores/<int:devedor_id>/titulos/', listar_titulos_por_devedor, name='listar_titulos_por_devedor'),
    path('devedores/<int:devedor_id>/titulos/', views.listar_titulos_por_devedor, name='titulos_listar_por_devedor'),
    path('titulos/', views.titulos_listar, name='titulos_listar'),
    path('titulos/adicionar/', views.adicionar_titulo, name='adicionar_titulo'),
    path('titulos/<int:id>/editar/', views.editar_titulo, name='editar_titulo'),
    path('titulos/<int:id>/excluir/', views.excluir_titulo, name='excluir_titulo'),
    path('login/', views.login_view, name='login'),
    path("followups/", views.followups_listar, name="followups_listar"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('titulos/<int:titulo_id>/acordo/', views.realizar_acordo, name='realizar_acordo'),    
    path('acordos/listar/', views.listar_acordos, name='acordos_listar'),
    path('parcelamentos/', views.listar_parcelamentos, name='listar_parcelamentos'),
    path('parcelamentos/pagar/<int:parcela_id>/', pagar_parcela, name='pagar_parcela'),     
    path('titulos/<int:titulo_id>/baixar/', views.realizar_baixa, name='realizar_baixa'),
    path('devedores/<int:devedor_id>/adicionar-titulo/', views.adicionar_titulo_pg_devedor, name='adicionar_titulo_pg_devedor'),
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('agendamentos/criar/', views.criar_agendamento, name='criar_agendamento'),
    path('agendamentos/<int:agendamento_id>/editar/', views.editar_agendamento, name='editar_agendamento'),
    path('agendamentos/<int:agendamento_id>/excluir/', views.excluir_agendamento, name='excluir_agendamento'),
    path('agendamentos/finalizar/<int:agendamento_id>/', views.finalizar_agendamento, name='finalizar_agendamento'),
     path('parcelamentos/<int:parcelamento_id>/', detalhar_parcela, name='detalhar_parcela'),
     path('detalhes-devedor/<int:titulo_id>/', views.detalhes_devedor, name='detalhes_devedor'),

     path('editar-telefones/<int:devedor_id>/', views.editar_telefones, name='editar_telefones'),
     path('lista-titulos/', views.lista_titulos, name='lista_titulos'),
       
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('usuarios/adicionar/', adicionar_usuario, name='adicionar_usuario'),
    path('usuarios/<int:user_id>/editar/', editar_usuario, name='editar_usuario'),
    path('usuarios/<int:user_id>/excluir/', excluir_usuario, name='excluir_usuario'),
     path('grupos/', listar_grupos, name='listar_grupos'),  # Para listar os grupos
    path('grupos/<int:grupo_id>/editar/', editar_grupo, name='editar_grupo'),  # Para editar um grupo
    path('grupos/atualizar-permissao/', atualizar_permissao, name='atualizar_permissao'),
    path('titulos/<int:titulo_id>/gerar_pdf/', views.gerar_pdf, name='gerar_pdf'),
     path("baixar_modelo_devedor/", views.baixar_modelo_devedor, name="baixar_modelo_devedor"),
    path("importar_devedor/", views.importar_devedor, name="importar_devedor"),
    path('gerar-recibo/<int:titulo_id>/', views.gerar_recibo, name='gerar_recibo'),
    path('acordos/<int:titulo_id>/gerar_contrato/', views.gerar_contrato, name='gerar_contrato'),
    path('adicionar-follow-up/<int:devedor_id>/', views.adicionar_follow_up, name='adicionar_follow_up'),
    path('listar-follow-ups/<int:devedor_id>/', views.listar_follow_ups, name='listar_follow_ups'),
    path('logs/', views.listar_logs, name='listar_logs'),    
    path('parcelamento/<int:parcela_id>/anexar-comprovante/', views.anexar_comprovante, name='anexar_comprovante'),
    path('baixar_comprovante/<int:parcelamento_id>/', views.baixar_comprovante, name='baixar_comprovante'),
    path('mensagens/', views.listar_mensagens, name='listar_mensagens'),    
    path('mensagens/adicionar/', views.adicionar_mensagem, name='adicionar_mensagem'),
    path('mensagens/editar/<int:pk>/', views.editar_mensagem, name='editar_mensagem'),
    path('mensagens/excluir/<int:pk>/', views.excluir_mensagem, name='excluir_mensagem'),
    path('tabelas/', views.tabelas_listar, name='tabelas_listar'),  # Lista de tabelas
    path('tabelas/adicionar/', views.tabela_adicionar, name='tabela_adicionar'),  # Formulário para adicionar tabela
    path('tabelas/editar/<int:tabela_id>/', views.tabela_editar, name='tabela_editar'),  # Formulário para editar tabela
    path('tabelas/excluir/<int:tabela_id>/', views.tabela_excluir, name='tabela_excluir'),  # Excluir tabela

    # Rotas para gerenciamento de itens da lista
    path('tabelas/<int:tabela_id>/itens/', views.lista_gerenciar, name='lista_gerenciar'),  # Gerenciamento de itens da lista
    path('tabelas/<int:tabela_id>/itens/adicionar/', views.lista_adicionar, name='lista_adicionar'),  # Adicionar item à lista
   
    path('tabelas/<int:tabela_id>/itens/editar/<int:item_id>/', views.lista_editar, name='lista_editar'),

    path('tabelas/<int:tabela_id>/itens/excluir/<int:item_id>/', views.lista_excluir, name='lista_excluir'),  # Excluir item da lista
     path('finalizar-titulo/<int:titulo_id>/', views.finalizar_titulo, name='finalizar_titulo'),
     path('quitar-parcela/<int:titulo_id>/', views.quitar_parcela, name='quitar_parcela'),
     path('titulos/quitados/', views.quitados_listar, name='quitados_listar'),
     # API interna para buscar dados na Lemit pelo CPF
     path('api/devedores/buscar-por-cpf/', views.consultar_cpf_lemit, name='consultar_cpf_lemit'),
     
     #Anexar e baixar contrato
     path('anexar-contrato/<int:titulo_id>/', views.anexar_contrato, name='anexar_contrato'),
     
   
  
    

     
     

     
    


   



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
