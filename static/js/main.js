'use strict';

var app = angular.module('cravattdb', ['ngRoute', 'angularFileUpload']);

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

app.controller('AddController', ['$scope', 'FileUploader', function($scope, FileUploader) {
    var uploader = $scope.uploader = new FileUploader();

    uploader.onBeforeUploadItem = function(item) {
        item.formData = [ $scope.data ];
    }

    $scope.addDataset = function() {
        uploader.uploadAll();
    }
}]);