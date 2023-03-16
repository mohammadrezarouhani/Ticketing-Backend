from django.shortcuts import render


# class UserViewSet(ModelViewSet):
#     http_method_names=['get','delete']
#     permission_classes=[IsAuthenticated]
#     serializer_class=serializer.BaseUserSerializer
#     queryset=models.BaseUser.objects.select_related('departman').all()

#     def get_queryset(self):
#         queryset=super().get_queryset()
#         username=self.request.query_params.get('username')
#         firstname=self.request.query_params.get('firstname')
#         lastname=self.request.query_params.get('lastname')

#         if username or firstname or lastname:
#             queryset=queryset.filter(Q(username__icontains=username)|
#                                     Q(firstname__icontains=firstname)|
#                                     Q(lastname__icontains=lastname))
#         return queryset


# class UserUpdateView(ModelViewSet):
#     http_method_names=['put']
#     permission_classes=[IsAuthenticated]
#     serializer_class=serializer.UpdateUserSerializer
#     queryset=models.BaseUser.objects.select_related('departman').all()      
    
    
# class UserCreateView(ModelViewSet):
#     http_method_names=['post']
#     permission_classes=[IsAuthenticated]
#     serializer_class=serializer.CreateUserSerializer
#     queryset=models.BaseUser.objects.select_related('departman').all()       

