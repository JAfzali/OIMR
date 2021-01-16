import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import firebase from 'firebase'
import axios from 'axios'
import moment from 'moment'
import VuePaginate from 'vue-paginate'

Vue.use(VuePaginate)

Vue.prototype.moment = moment

Vue.config.productionTip = false

axios.defaults.baseURL = 'http://localhost:5000/'
/*
axios.interceptors.request.use(config => {
  store.dispatch('loading', true)
  return config
})

axios.interceptors.response.use(config => {
  store.dispatch('loading', false)
  return config
}) */

// Your web app's Firebase configuration
let app = ''
var firebaseConfig = {
  apiKey: 'AIzaSyAKizEeV4uMXuI_oYIhoBt2Hk5z2l__KWk',
  authDomain: 'rackinventory.firebaseapp.com',
  databaseURL: 'https://rackinventory.firebaseio.com',
  projectId: 'rackinventory',
  storageBucket: 'rackinventory.appspot.com',
  messagingSenderId: '1033834698833',
  appId: '1:1033834698833:web:03434fb912c4e0868f4070',
  measurementId: 'G-6Q4FFFZSG4'
}
// Initialize Firebase
firebase.initializeApp(firebaseConfig)
firebase.analytics()

firebase.auth().onAuthStateChanged(() => {
  if (!app) {
    app = new Vue({
      router,
      store,
      vuetify,
      render: h => h(App)
    }).$mount('#app')
  }
})
