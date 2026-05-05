Phase 1: Core Request/ Response Cycle
1. Requests
2. Responses
3. Status Codes
4. APIView

Phase 2: Data Handling
5. Parsers
6. Renderers
7. Content Negotiation

Phase 3: Serialization 
8. Serializers
9. ModelSerializers
10. Validation

Phase 4: Views & Architecture
11. Function-Based Views
12. Class-Based Views
13. Generic Views
14. ViewSets

Phase 5: Authentication & Permissions
15. Authentication
16. Permissions
17. Throttling

Phase 6: Advanced API Behavior
18. Filtering
19. Pagination
20. ersioning

Phase 7: Production Concerns
21. CORS
22. API Documentation
23. Testing

===================================================
What is a request in drf
in normal django
request.POST
request.GET

drf
request = Request()

Handle JSON
Handle PUT/PATCH/DELETE
Handle authentication
Handle content negotiation

request.data
------------
DRF:
Checks Content-Type
Chooses parser
Converts body → Python data

request.query_params
--------------------

request.user
------------
request.auth
------------

request.method
--------------
request.content_type
--------------------

request.stream
--------------

==================================================

Responses:

HttpResponse
------------
works onyl for plain text / html
no automatic json handling
no api friendly formatting

Response:
---------

DRF Response = Python data -> automatically converted to API response.

Python dict → Renderer → JSON → HTTP Response

Handles:
JSON conversion
Content negotiation
Status codes
Headers

Converts Python → JSON (like JsonResponse)
BUT ALSO:
Supports multiple formats (not just JSON)
Uses renderers
Works with serializers
Integrates with authentication, permissions
Supports Browsable API

Converts Python data → final output format (JSON / HTML / etc.)


===================================================

Status Codes:

Request -> Server -> Response + Status Code

==================================================

Function based views
---------------------
@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass

Class Based views
------------------
class MyView(APIView):

    def get(self, request):
        return Response({"msg": "GET"})

    def post(self, request):
        return Response({"msg": "POST"})
===================================================

Generic views:
-------------

perform_create
perform_update
perform_destroy

get_queryset
get_object

get_serializer_class
get_serializer
get_serializer_context

create
update
destroy

filter_queryset
paginate_queryset
get_permissions
initial
finalize_response

method based thinking

==================================================

viewsets:
--------

Avoid Repetition on queryset , serializer and permissions

viewset came

list()
create()
retrieve()
update()
destroy()

all functions inside generic views

it is working based on action

Action based thinking
===================================================

APIView -> maximum control
Generic Views  -> balance
Viewsets -> maximum automation

===================================================

Model -> Python object -> Json for response -> Deserialization
Json -> Python object -> Model for request -> serialization

serializer = converter + validator

Request -> request.data -> Serializer -> validated_data -> dave()

Model -> serializer -> serializer.data -> Response