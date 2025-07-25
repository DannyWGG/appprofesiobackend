from ninja_extra                                import NinjaExtraAPI

from django_rest_passwordreset.controller       import ResetPasswordController

from apps.frontend.views                        import router as servicio_router

from apps.cuenta.views.profile                  import router as profile_router
from apps.cuenta.views.change_email             import router as change_email_router
from apps.cuenta.views.change_question_answer   import router as change_question_answer_router
from apps.cuenta.views.create_account           import router as create_account_router
from apps.cuenta.views.change_password          import router as change_password_router
from apps.cuenta.views.change_roles             import router as update_roles_router
from apps.cuenta.views.create_account           import CreateUserController
from apps.cuenta.views.login                    import MyTokenObtainPairController

from apps.geo.views.estado                      import router as estado_router
from apps.geo.views.municipio                   import router as municipio_router
from apps.geo.views.parroquia                   import router as parroquia_router

from apps.saime.views.saime                     import router as saime_router

api = NinjaExtraAPI(
                        title           = "profesio",
                        description     = "API de profesio",
                        urls_namespace  = "profesio",
                    )


api.add_router("/servicio/",    servicio_router)

api.add_router("/auth/",        change_password_router)
api.add_router("/auth/",        change_email_router)
api.add_router("/auth/",        change_question_answer_router)
api.add_router("/auth/",        update_roles_router)
api.add_router("/auth/",        create_account_router)
api.add_router("/auth/",        profile_router)

api.add_router("/geo/",         estado_router)
api.add_router("/geo/",         municipio_router)
api.add_router("/geo/",         parroquia_router)

api.add_router("/saime/",       saime_router)

api.register_controllers(CreateUserController)
api.register_controllers(ResetPasswordController)
api.register_controllers(MyTokenObtainPairController)
