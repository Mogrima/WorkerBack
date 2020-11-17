import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from work.models import Workers


class OccupationType(DjangoObjectType):
    class Meta:
        model = Workers

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


class WorkersInput(graphene.InputObjectType):
    name = graphene.String()
    companyName = graphene.String()
    position_name = graphene.String()
    hireDate = graphene.Date()
    fireDate = graphene.Date()
    salary = graphene.Int()
    fraction = graphene.Int()
    base = graphene.Int()
    advance = graphene.Int()
    by_hours = graphene.Boolean()

class addOccupation(graphene.Mutation):
    class Arguments:
      input = WorkersInput(required=True)

    ok = graphene.Boolean()
    worker = graphene.Field(OccupationType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        worker_instance = Workers(
            name=input.name,
            companyName=input.companyName,
            position_name=input.position_name,
            hire_date=input.hireDate,
            fire_date=input.fireDate,
            salary=input.salary,
            fraction=input.fraction,
            base=input.base,
            advance=input.advance,
            by_hours=input.by_hours
        )
        worker_instance.save()
        return addOccupation(worker=worker_instance)


class updateOccupation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = WorkersInput(required=True)

    ok = graphene.Boolean()
    worker = graphene.Field(OccupationType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        worker_instance = Workers.objects.get(pk=id)
        if worker_instance:
            ok = True
            worker_instance.salary = input.salary
            worker_instance.fraction = input.fraction
            worker_instance.base = input.base
            worker_instance.advance = input.advance
            worker_instance.save()
            return updateOccupation(ok=ok, worker=worker_instance)
        return updateOccupation(ok=ok, worker=None)


class Mutation(graphene.ObjectType):
    add_occupation = addOccupation.Field()
    update_occupation = updateOccupation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
