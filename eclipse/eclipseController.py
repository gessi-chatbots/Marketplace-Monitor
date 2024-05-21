import json
import requests
from . import EclipseJSONParser
from django.http import JsonResponse
from MonitoringSoftwareMarketplaces.controllerInterface import controllerInterface
from . import eclipseReposiroty

class EclipseController(controllerInterface):

    def getCategoriesMarketplace(request):
        data = json.loads(request.body)
        cache = data.get('cache')
        pageNumber = data.get('page_num') or 1
        params = {'page_num': pageNumber}  
        if(cache):
            categories = eclipseReposiroty.getCategories()
            markets = eclipseReposiroty.getMarkets()
            return JsonResponse({'categories': categories, 'markets': markets}, safe=False,status=201)
       
        # Si no se especifica el parámetro cache, o si es falso, se hace la petición a la API
        response = requests.get('https://marketplace.eclipse.org/api/p', params=params)
        if response.status_code == 200:
            try:
                categories = EclipseJSONParser.EclipseJSONParser.extractCategories(response)
                #eclipseReposiroty.insertCategories(categories)
                markets = EclipseJSONParser.EclipseJSONParser.extractMarkets(response)
                #eclipseReposiroty.insertMarkets(markets)
                # Aqui se deberian de meter en la base de datos 
                response.json = {'categories': categories, 'markets': markets}
                return JsonResponse(response.json, safe=False,status=202)
            
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Error al decodificar JSON en la respuesta'})
            
        else:
            # Si la respuesta no fue exitosa, regresar un mensaje de error con el código de estado
            return JsonResponse({'error': f'Solicitud no exitosa. Código de estado: {response.status_code}'})
        
    def getProductsByMarketplaceAndCategory(request, market, category):
        data = json.loads(request.body)
        cache = data.get('cache')
        pageNumber = data.get('page_num') or 1
        params = {'page_num': pageNumber}  
        if(cache):
            products = eclipseReposiroty.getProducts(market, category)
            return JsonResponse(products, safe=False,status=201)
        # Si no se especifica el parámetro cache, o si es falso, se hace la petición a la API
        response = requests.get('https://marketplace.eclipse.org/taxonomy/term/{},{}/api/p'.format(category, market), params=params)
        if response.status_code == 200:
            try:
                products = EclipseJSONParser.EclipseJSONParser.extractProductsByParameter(response,"Category")
                # Aqui se deberian de meter en la base de datos
                return JsonResponse(products, safe=False,status=202)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Error al decodificar JSON en la respuesta'},status=response.status_code)
        else:
            # Si la respuesta no fue exitosa, regresar un mensaje de error con el código de estado
            return JsonResponse({'error': f'Solicitud no exitosa. Código de estado: {response.status_code}'}, status=response.status_code)

    def getProductById(request, nodeId):
        data = json.loads(request.body)
        cache = data.get('cache')
        pageNumber = data.get('page_num') or 1
        params = {'page_num': pageNumber}  
        if(cache):
            product = eclipseReposiroty.getProductById(nodeId)
            return JsonResponse(product, safe=False,status=201)
        # Si no se especifica el parámetro cache, o si es falso, se hace la petición a la API
        response = requests.get('https://marketplace.eclipse.org/node/{}}/api/p'.format(nodeId), params=params)
        if response.status_code == 200:
            try:
                info = response.text
                product = EclipseJSONParser.EclipseJSONParser.extractSingleProduct(response)
                return response
            except json.JSONDecodeError:
                return {'error': 'Error al decodificar JSON en la respuesta'}
        else:
            # Si la respuesta no fue exitosa, regresar un mensaje de error con el código de estado
            print( response.status_code)
            return {'error': f'Solicitud no exitosa. Código de estado: {response.status_code}'}
        
    def getProductByTitle(request):
        pageNumber = request.GET.get('page_num') or 1
        title = request.GET.get('title')
        params = {'page_num': pageNumber}  
        response = requests.get('https://marketplace.eclipse.org/content/{}'.format(title), params=params)
        
        if response.status_code == 200:
            try:
                info = response.text
                return response
            except json.JSONDecodeError:
                return {'error': 'Error al decodificar JSON en la respuesta'}
        else:
            # Si la respuesta no fue exitosa, regresar un mensaje de error con el código de estado
            print( response.status_code)
            return {'error': f'Solicitud no exitosa. Código de estado: {response.status_code}'}
        
    def getTopFavorites(request):
        pageNumber = request.GET.get('page_num') or 1
        params = {'page_num': pageNumber}  

        response = requests.get('https://marketplace.eclipse.org/favorites/top/api/p', params=params)
        
        if response.status_code == 200:
            try:
                products = EclipseJSONParser.EclipseJSONParser.extractProductsByParameter(response,"favorites")
                # Aqui se deberian de meter en la base de datos
                return response
            except json.JSONDecodeError:
                return {'error': 'Error al decodificar JSON en la respuesta'}
        else:
            # Si la respuesta no fue exitosa, regresar un mensaje de error con el código de estado
            print( response.status_code)
            return {'error': f'Solicitud no exitosa. Código de estado: {response.status_code}'}
        
    def getProductByQuery(request, query):
        pageNumber = request.GET.get('page_num') or 1
        filters = request.GET.get('filters') 
        params = {'page_num': pageNumber}  

        response = requests.get('http://marketplace.eclipse.org/api/p/search/apachesolr_search/{}'.format(query), params=params)
        
        if response.status_code == 200:
            try:
                products = EclipseJSONParser.EclipseJSONParser.extractProductsByParameter(response,"search")
                # Aqui se deberian de meter en la base de datos
                return response
            except json.JSONDecodeError:
                return {'error': 'Error al decodificar JSON en la respuesta'}
        else:
            # Si la respuesta no fue exitosa, regresar un mensaje de error con el código de estado
            print( response.status_code)
            return {'error': f'Solicitud no exitosa. Código de estado: {response.status_code}'}