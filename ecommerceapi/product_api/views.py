from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from product_api.models import Product, Order, OrderDetail
from product_api.serializers import ProductSerializer, OrderSerializer, OrderDetailSerializer

# Create your views here.

# CREATE VIEWSET FOR PRODUCT MODEL
class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling CRUD operations on the Product model.

    Inherits from viewsets.ModelViewSet, which provides default implementations for
    the create, retrieve, update, partial_update, and destroy actions.

    Attributes:
        queryset (QuerySet): The queryset of all Product objects.
        serializer_class (Serializer): The serializer class for Product objects.

    Methods:
        create(request, *args, **kwargs): Create a new Product object.
        list(request, *args, **kwargs): Retrieve a list of all Product objects.
        destroy(request, *args, **kwargs): Delete a Product object.
        update(request, *args, **kwargs): Update a Product object.
        partial_update(request, *args, **kwargs): Partially update a Product object.
        perform_destroy(instance): Perform the deletion of a Product object.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new Product object.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object containing the serialized data of the created Product object.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request, *args, **kwargs):
        """
        Retrieve a list of all Product objects.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object containing the serialized data of the Product objects.
        """
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        """
        Delete a Product object.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object indicating the success or failure of the deletion.
        """
        instance = self.get_object()
        if instance.stock > 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        """
        Update a Product object.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object containing the serialized data of the updated Product object
                      or the error message if the update fails.
        """
        product = self.get_object()
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, *args, **kwargs):
        """
        Partially update a Product object.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object containing the serialized data of the updated Product object
                      or the error message if the update fails.
        """
        instance = self.get_object()
        if instance.is_valid():
            self.perform_update(instance)
            return Response(instance.data)
        else:
            return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_destroy(self, instance):
        """
        Perform the deletion of a Product object.

        Args:
            instance (Product): The Product object to be deleted.

        Returns:
            None
        """
        instance.delete()

    
# CREATE VIEWSET FOR ORDER MODEL
class OrderViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling CRUD operations on Order objects.

    Inherits from viewsets.ModelViewSet which provides default implementations for
    the standard CRUD operations (create, retrieve, update, partial_update, destroy).

    Attributes:
        queryset (QuerySet): The queryset of Order objects.
        serializer_class (Serializer): The serializer class for Order objects.
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new Order object.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object with the serialized Order data.

        Raises:
            HTTP_400_BAD_REQUEST: If the request data is invalid.
        """
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Delete an existing Order object.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object with no content.

        Raises:
            HTTP_404_NOT_FOUND: If the Order object does not exist.
        """
        order = self.get_object()
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        """
        Update an existing Order object.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object with the serialized Order data.

        Raises:
            HTTP_400_BAD_REQUEST: If the request data is invalid.
            HTTP_404_NOT_FOUND: If the Order object does not exist.
        """
        order = self.get_object()
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update an existing Order object.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: The HTTP response object with the serialized Order data.

        Raises:
            HTTP_400_BAD_REQUEST: If the request data is invalid.
            HTTP_404_NOT_FOUND: If the Order object does not exist.
        """
        order = self.get_object()
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

# CREATE VIEWSET FOR ORDERDETAIL MODEL
class OrderDetailViewSet(viewsets.ModelViewSet):
    """
    A viewset for handling CRUD operations on OrderDetail objects.
    """

    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new OrderDetail object.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            A Response object with the serialized data of the created OrderDetail object,
            or a Response object with the validation errors if the data is invalid.
        """
        serializer = OrderDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        """
        Delete an existing OrderDetail object.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            A Response object with a status code indicating the success of the deletion.
        """
        orderdetail = self.get_object()
        orderdetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        """
        Update an existing OrderDetail object.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            A Response object with the serialized data of the updated OrderDetail object,
            or a Response object with the validation errors if the data is invalid.
        """
        orderdetail = self.get_object()
        serializer = OrderDetailSerializer(orderdetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def partial_update(self, request, *args, **kwargs):
        """
        Partially update an existing OrderDetail object.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            A Response object with the serialized data of the partially updated OrderDetail object,
            or a Response object with the validation errors if the data is invalid.
        """
        orderdetail = self.get_object()
        serializer = OrderDetailSerializer(orderdetail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
