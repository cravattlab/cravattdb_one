'use strict';

var app = angular.module('cravattdb', ['ngRoute', 'angularFileUpload']);

app.value('bootstrap', window.bootstrap);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider.when('/add', {
        templateUrl: '/static/partials/add.html',
        controller: 'AddController',
        controllerAs: 'add'
    });

    $locationProvider.html5Mode(true);
}]);

app.controller('ListController', ['$scope', function($scope) {

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