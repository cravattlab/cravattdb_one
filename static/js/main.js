'use strict';

var app = angular.module('cravattdb', ['angularFileUpload']);

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