'use strict';

var app = angular.module('cravattdb', ['angularFileUpload']);

app.controller('ListController', ['$scope', function($scope) {

}]);

app.controller('AddController', ['$scope', 'FileUploader', function($scope, FileUploader) {
    $scope.uploader = new FileUploader();

    $scope.addDataset = function(data) {
        console.log(data);
    }
}]);