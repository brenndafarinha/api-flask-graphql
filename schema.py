import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Users as UsersModel


class Users(SQLAlchemyObjectType):
    class Meta:
        model = UsersModel
        interfaces = (relay.Node, )


class UsersConnection(relay.Connection):
    class Meta:
        node = Users


class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
        phone = graphene.String()


    new_user = graphene.Field(lambda: Users)

    def mutate(root, info, name, username, email, password, phone):
        new_user = Users(name=name, username=username, email=email, password=password, phone=phone)
        return CreateUser(new_user=new_user)


class User(graphene.ObjectType):
    name = graphene.String()
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()
    phone = graphene.String()


class Query(graphene.ObjectType):
    user = graphene.Field(User)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
