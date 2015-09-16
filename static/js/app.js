var app = angular.module('App',[]);

app.config(function($interpolateProvider) { 
	$interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});


app.factory('socket', function($rootScope) {
    var socket = io.connect('http://localhost:3000');
    return {
        on: function(eventName, callback) {
            socket.on(eventName, function() {
                var args = arguments;
                $rootScope.$apply(function() {
                    callback.apply(socket, args);
                });
            });
        },
        emit: function(eventName, data, callback) {
            socket.emit(eventName, data, function() {
                var args = arguments;
                $rootScope.$apply(function() {
                    if(callback) {
                        callback.apply(socket, args);
                    }
                });
            });
        }
    };
});


app.controller('AppCtrl', function ($scope,socket) {

    $scope.datos=[];

    $scope.Comentar = function (){
        var datos = {
            user: $scope.user,
            comment: $scope.comment
        }
        console.info(datos);
        socket.emit('guardar comentario', datos);
        $scope.comment="";
    }

    socket.on('devolviendo', function(data){
        var data= JSON.parse(data)
        console.log(data);
        $scope.datos.push(data);
        console.info($scope.datos);
    });

    
})