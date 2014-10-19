'use strict';

var app = angular.module('cravattdb', ['ngRoute', 'ngResource', 'angularFileUpload', 'pasvaz.bindonce']);

app.value('bootstrap', window.bootstrap || {});

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $locationProvider.html5Mode(true);
    $routeProvider.when('/add', {
        templateUrl: '/static/partials/add.html',
        controller: 'AddController',
        controllerAs: 'add'
    })
    .when('/list', {
        templateUrl: '/static/partials/list.html',
        controller: 'ListController',
        controllerAs: 'list' 
    })
    .when('/dataset/:id', {
        templateUrl: '/static/partials/dataset.html',
        controller: 'DatasetController',
        controllerAs: 'dataset'
    });

}]);


app.controller('DatasetController', ['$scope', 'bootstrap', '$http', '$routeParams', function($scope, bootstrap, $http, $routeParams) {
    this.predicate = 'ipi';

    if (bootstrap.dataset) {
        this.bootstrap = bootstrap.dataset
    } else {
        $http.get('/api/dataset/' + $routeParams.id).success(function(data) {
            this.bootstrap = data.list;
        }.bind(this));    
    }

    this.sorter = function(item) {
        return item[this.predicate];
    }.bind(this);
}]);

app.controller('ListController', ['$scope', 'bootstrap', '$location', '$resource', '$http', function($scope, bootstrap, $location, $resource, $http) {
    this.predicate = '';

    if (bootstrap.list) {
        this.bootstrap = bootstrap.list;
    } else {
        $http.get('/api/list').success(function(data) {
            this.bootstrap = data.list;
        }.bind(this));
    }
    // this.bootstrap = bootstrap.list || $resource('/api/list').get().list;

    this.sorter = function(item) {
        return item[this.predicate];
    }.bind(this);

    this.showDataset = function(id) {
        $location.path('/dataset/' + id);
    };
}]);

app.controller('AddController', ['$scope', 'FileUploader', 'bootstrap', function($scope, FileUploader, bootstrap) {
    var uploader = $scope.uploader = new FileUploader({ url : '/add' });

    this.bootstrap = bootstrap;
    $scope.data = {};

    uploader.onBeforeUploadItem = function(item) {
        item.formData = [ $scope.data ];
    };

    $scope.addDataset = function() {
        uploader.uploadAll();
    };
}]);