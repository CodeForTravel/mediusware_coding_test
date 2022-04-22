import Vue from "vue";

Vue.filter('lowercase', function (value) {
    return value.toLowerCase()
})

Vue.filter('uppercase', function (value) {
    return value.toUpperCase()
})

Vue.filter('capitalize', function (value) {
    return value.charAt(0).toUpperCase() + value.slice(1);
})