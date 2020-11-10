import graphene
from graphene_django.types import DjangoObjectType, ObjectType
# from graphene_django.types import DjangoObjectType
from work.models import Workers
from graphene_django.filter import DjangoFilterConnectionField


class OccupationType(DjangoObjectType):
    class Meta:
        model = Workers


class WorkersInput(graphene.InputObjectType):
    name = graphene.String(required=True, null=False)
    companyName = graphene.String(required=True)
    position_name = graphene.String(required=True)
    hireDate = graphene.Date(required=True)
    fireDate = graphene.Date()
    salary = graphene.Int(required=True)
    fraction = graphene.Int(required=True)
    base = graphene.Int(required=True)
    advance = graphene.Int(required=True)
    by_hours = graphene.Boolean(required=True)

class CreateWorker(graphene.Mutation):
    worker = graphene.Field(OccupationType)

    # class Input:
    #     name = graphene.String()
        # companyName = graphene.String()
        # positionName = graphene.String()
        # hireDate = graphene.Date()
        # fireDate = graphene.Date()
        # salary = graphene.Int()
        # fraction = graphene.Int()
        # base = graphene.Int()
        # advance = graphene.Int()
        # by_hours = graphene.Boolean()

#     def mutate_and_get_payload(self, root, info, **input):
#         worker = Workers(
#             name=input.get('name')
#         )

#         worker.save()

#         return CreateWorker(worker=worker)

# class Mutation(graphene.ObjectType):
#     create_worker = CreateWorker.Field()
    class Arguments:
      input = WorkersInput(required=True)
    #   ok = graphene.Boolean()
      OccupationType

    @staticmethod
    def mutate(root, info, input=None):
        # ok = True
        worker_instance = Workers(
          name = input.name,
          companyName = input.companyName,
          position_name = input.position_name,
          hire_date = input.hireDate,
          fire_date = input.fireDate,
          salary = input.salary,
          fraction = input.fraction,
          base = input.base,
          advance = input.advance,
          by_hours = input.by_hours
        )
        worker_instance.save()
        return CreateWorker(worker=worker_instance)

class Mutation(graphene.ObjectType):
    create_worker = CreateWorker.Field()

class Query(ObjectType):
    getOccupation = graphene.Field(OccupationType, id=graphene.Int())
    getOccupations = graphene.List(OccupationType)

    def resolve_getOccupation(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Workers.objects.get(pk=id)
        return None

    def resolve_getOccupations(self, info, **kwargs):
        return Workers.objects.all()

    
schema = graphene.Schema(query=Query, mutation=Mutation)
# schema = graphene.Schema(query=Query)
