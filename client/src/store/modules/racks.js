import axios from 'axios'

const state = {
  racksAndPipes: [],
  AdminRacks: []
}

const getters = {
  getracksAndPipes: state => state.racksAndPipes,
  getAdminRacks: state => state.AdminRacks
}

const actions = {
  fetchracksAndPipes ({ commit, rootGetters }) {
    let rackresponse = ''
    console.log('user: ' + rootGetters.getUsername)
    rackresponse = axios.get('/getPipesAndRacks', {
      params: { username: rootGetters.getUsername }
    })
    rackresponse
      .then(response => {
        console.log(response.data)
        commit('setracksAndPipes', response.data)
      })
      .catch(err => {
        console.log('Feil ved henting av racks' + '\n' + err)
      })
  },
  clearracksAndPipes ({ commit }) {
    commit('removeracksAndPipes')
  },
  fetchAdminRacks ({ commit, rootGetters }) {
    let adminrackresponse = ''
    console.log('user:' + rootGetters.getUsername)
    adminrackresponse = axios.get('getAllRacks', {
      params: { username: rootGetters.getUsername }
    })
    adminrackresponse
      .then(response => {
        console.log(response.data)
        commit('setAdminRacks', response.data)
      })
      .catch(err => {
        console.log('Feil ved henting av adminracks' + '\n' + err)
      })
  },
  clearAdminRacks ({ commit }) {
    commit('removeAdminRacks')
  }
}

const mutations = {
  setracksAndPipes: (state, racks) => (state.racksAndPipes = racks),
  removeracksAndPipes: state => (state.racksAndPipes = []),
  setAdminRacks: (state, racks) => (state.AdminRacks = racks),
  removeAdminRacks: state => (state.AdminRacks = [])
}

export default {
  state,
  getters,
  actions,
  mutations
}
