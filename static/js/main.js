'use strict';

var app = angular.module('cravattdb', ['ngRoute', 'ngResource', 'angularFileUpload', 'pasvaz.bindonce', 'datatables']);

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

app.controller('NavController', ['$location', function($location) {
    this.classes = function(page) {
        if (page === $location.path()) {
            return 'active';
        }
    }
}]);

app.controller('DatasetController', [
    '$scope',
    'bootstrap',
    '$http',
    '$routeParams',
    'DTOptionsBuilder',
    'DTColumnBuilder',
    '$resource',
function($scope, bootstrap, $http, $routeParams, DTOptionsBuilder, DTColumnBuilder, $resource) {


    this.dtOptions = DTOptionsBuilder
        .fromSource('/api/dataset/' + $routeParams.id)
        .withDataProp('dataset.data')
        .withBootstrap();

    setDefaults(this.dtOptions);

    this.dtOptions.aoColumns = extractColumns(["peptide_index", "ipi", "symbol", "sequence", "mass", "charge", "segment", "ratio"]);

    function setDefaults(options) {
        options.pageLength = 25;
        // options.paging = false;
        options.autoWidth = true;
        options.lengthMenu = [ [10, 25, 50, -1], [10, 25, 50, "All"] ];
        options.deferRender = true;
    }

    function extractColumns(headers) {
        var columns = [];
        for (var i = 0, n = headers.length; i < n; i++) {
            columns.push({ sTitle: headers[i] });
        }
        return columns;
    }
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

app.controller('AddController', ['$scope', 'FileUploader', 'bootstrap', '$http', function($scope, FileUploader, bootstrap, $http) {
    var uploader = $scope.uploader = new FileUploader({ url : '/add' });

    if (bootstrap.add) {
        this.bootstrap = bootstrap.add;
    } else {
        $http.get('/api/add').success(function(data) {
            this.bootstrap = data.add;
        }.bind(this));  
    }

    $scope.data = {};

    uploader.onBeforeUploadItem = function(item) {
        item.formData = [ $scope.data ];
    };

    $scope.addDataset = function() {
        uploader.uploadAll();
    };
}]);