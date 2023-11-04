import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(argument=graphene.String(default_value='world'))

    def resolve_hello(self, info, argument):
        print("AB")
        request = info.context
        print(request.META)
        return "hello {0} - [{1}]".format(request.META['REMOTE_ADDR'], request.META['REMOTE_ADDR'])


schema = graphene.Schema(query=Query)