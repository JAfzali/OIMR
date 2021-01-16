import firebase from 'firebase'
import axios from 'axios'
import router from '../../router/index.js'

const state = {
  email: '',
  username: '',
  loadingcomplete: false,
  assetlist: [],
  asset: null
}

const getters = {
  getEmail: state => state.email,
  getAuth: state => !!state.email,
  getUsername: state => state.username,
  getLoadingcomplete: state => state.loadingcomplete,
  getAssetlist: state => state.assetlist,
  getAsset: state => state.asset
}

const actions = {
  loading ({ commit }, value) {
    commit('loading', value)
  },
  fetchEmail ({ commit }) {
    const email = firebase.auth().currentUser.email
    const pack = email
    commit('eMail', pack)
  },
  logOut ({ commit, dispatch }) {
    dispatch('clearracksAndPipes')
    dispatch('clearAdminRacks')
    commit('setLoadingcomplete',false)
    commit('logout')
  },
  fetchUsername ({ commit }, { usrname }) {
    let usrnameresponse = ''
    usrnameresponse = axios.post('/fetchUserName', { usrname })
    usrnameresponse.then(response => {
      console.log(response.data)
      commit('setUsername', response.data)
      commit('setAssetList',response.data)
      if(response.data.assetlist.length > 0) {
        router.replace('asset')
      } else {
        router.replace('home')
      }
      commit('setLoadingcomplete',true)
    })
      .catch(err => {
        console.log('Feil ved henting av brukernavn' + '\n' + err)
      })
  },
  setassetlist ({ commit }, {list}) {
    commit('setAssetList',list)
  },
  setasset ({ commit }, { asset }) {
    commit('setAsset',asset)
  } 

}

const mutations = {
  eMail: (state, pack) => {
    state.email = pack
  },
  logout: (state) => {
    state.email = ''
    state.username = ''
    state.asset = '',
    state.assetlist = []
  },
  setUsername: (state, data) => {
    state.username = data.username
  },
  loading: (state, value) => (state.loader = value),

  setAssetList: (state, data) => {
    state.assetlist = data.assetlist
  },
  setLoadingcomplete: (state, value) => {
    state.loadingcomplete = value
  },
  setAsset: (state, asset) => {
    state.asset = asset
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
