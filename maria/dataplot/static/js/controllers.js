'use strict';
angular.module('enquiryApp')

// .config(['$httpProvider', function($httpProvider) {
// 	console.log(csrf_token);
//     $httpProvider.defaults.headers.common['X-CSRFToken'] = csrf_token;
// }])

.controller('EnquiryController', ['$scope', 'dataFactory', function($scope, dataFactory) {

    //Step 1: Create a JavaScript object to hold the comment from the form
    $scope.status;
    $scope.statusCheck= false;
    $scope.enquiry = {};
    dataFactory.getCategories()
        .success(function (data) {
                $scope.categories = data;
                // $scope.enquiry.push($scope.enquiry);
                $scope.selected = $scope.categories[0];
            });
    dataFactory.getPrograms()
        .success(function (data) {
                $scope.programs = data;
                // $scope.enquiry.push($scope.enquiry);
                $scope.pselected = $scope.programs[0];

                console.log($scope.pselected);
            });
    


    $scope.submitEnquiry = function() {
console.log('called');
console.log($scope.pselected);
        $scope.enquiry.enquiry_category = $scope.selected.id;
        $scope.enquiry.program = $scope.pselected.id;
        dataFactory.insertEnquiry($scope.enquiry)
            .success(function () {
                $scope.status = 'Your enquiry is submitted successfully. we will get back to you soon';
                $scope.statusCheck = true;
                // $scope.enquiry.push($scope.enquiry);
            }).
            error(function(error) {
                $scope.status = 'Unable to insert Your: ' + error.message;
                $scope.statusCheck = false;
            });

        $scope.enquiry = {
            first_name: "",
            last_name: "",
            phone_number: "",
            email: "",
            address: "",
            previous_school: "",
            source: "",
            question: ""
        };
         dataFactory.getCategories()
        .success(function (data) {
                $scope.categories = data;
                // $scope.enquiry.push($scope.enquiry);
                $scope.selected = $scope.categories[0];
            });
        $scope.enquiryForm.$setPristine();

        dataFactory.getPrograms()
        .success(function (data) {
                $scope.programs = data;
                // $scope.enquiry.push($scope.enquiry);
                $scope.pselected = $scope.programs[0];
            });

        //Step 5: reset your JavaScript object that holds your comment
    };
}])

;
