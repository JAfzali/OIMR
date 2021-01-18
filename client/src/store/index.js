import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import racks from './modules/racks'
import createPersistedState from 'vuex-persistedstate'
Vue.use(Vuex)

export default new Vuex.Store({

  modules: {
    auth,
    racks
  },
  plugins: [
    createPersistedState({
      key: 'vuex-store',
      paths: [
        'auth.email',
        'auth.username',
        'auth.assetlist',
        'auth.loadingcomplete',
        'auth.asset',
        'auth.fleet'
      ]
    })
  ]
})
