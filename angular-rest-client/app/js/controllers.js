function Rest($scope, $http) {
		$http.get('http://localhost:8080/list').
        		success(function(data) {
            		$scope.list = data.list;
            		console.warn('GETLIST')
        	});
    	$scope.getRest= function(id){
    		$http.get('http://localhost:8080/documents/' + id).
        		success(function(data) {
            		$scope.data = data;
            		console.warn('GET')
        	});
        }
        $scope.putRest= function(){
    		$http.put('http://localhost:8080/documents',{
    			"_id":$scope.data.title,
    			"title":$scope.data.title,
    			"description":$scope.data.description,
    			"image":$scope.data.image,
    			"rating":$scope.data.rating
    		}).
        		success(function() {
            		console.warn('PUT')
        	});
        }
        $scope.deleteRest= function(){
    		$http.delete('http://localhost:8080/documents/' + $scope.data.title).
        		success(function() {
            		console.warn('DELETE')
        	});
        }
}