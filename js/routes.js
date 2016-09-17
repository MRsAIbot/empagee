angular.module('app.routes', [])

.config(function($stateProvider, $urlRouterProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider
    
  

      .state('takePhoto', {
    url: '/page1',
    templateUrl: 'templates/takePhoto.html',
    controller: 'takePhotoCtrl'
  })

  .state('login', {
    url: '/page3',
    templateUrl: 'templates/login.html',
    controller: 'loginCtrl'
  })

  .state('home', {
    url: '/page4',
    templateUrl: 'templates/home.html',
    controller: 'homeCtrl'
  })

  .state('patients', {
    url: '/page5',
    templateUrl: 'templates/patients.html',
    controller: 'patientsCtrl'
  })

  .state('signup', {
    url: '/page6',
    templateUrl: 'templates/signup.html',
    controller: 'signupCtrl'
  })

  .state('analyseExpression', {
    url: '/page7',
    templateUrl: 'templates/analyseExpression.html',
    controller: 'analyseExpressionCtrl'
  })

  .state('analysis', {
    url: '/page8',
    templateUrl: 'templates/analysis.html',
    controller: 'analysisCtrl'
  })

  .state('patient1', {
    url: '/page9',
    templateUrl: 'templates/patient1.html',
    controller: 'patient1Ctrl'
  })

$urlRouterProvider.otherwise('/page3')

  

});