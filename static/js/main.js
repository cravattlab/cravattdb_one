'use strict';

var app = angular.module('cravattdb', ['ngRoute', 'angularFileUpload']);

app.value('bootstrap', window.bootstrap);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
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

    $locationProvider.html5Mode(true);
}]);


app.controller('DatasetController', ['$scope', 'bootstrap', function($scope, bootstrap) {
    this.bootstrap = bootstrap;
}]);

app.controller('ListController', ['$scope', 'bootstrap', function($scope, bootstrap) {
    this.bootstrap = bootstrap;

    this.showDataset = function(id) {
        console.log('show dataset', arguments, id);
    }
}]);

app.controller('AddController', ['$scope', 'FileUploader', 'bootstrap', function($scope, FileUploader, bootstrap) {
    var uploader = $scope.uploader = new FileUploader({ url : '/add' });

    this.bootstrap = bootstrap;
    $scope.data = {};

    uploader.onBeforeUploadItem = function(item) {
        item.formData = [ $scope.data ];
    }

    $scope.addDataset = function() {
        uploader.uploadAll();
    }
}]);