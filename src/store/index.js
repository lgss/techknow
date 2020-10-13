import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    journey: null
  },

  getters: {
    journeyTitle: state => {
      if (state.journey)
        return `Questions about ${state.journey}`

      return null
    }
  },

  mutations: {
    setJourney(state, value) {
      state.journey = value
    }
  }
})