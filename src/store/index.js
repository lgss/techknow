import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    journey: null,
    pageContent: {}
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
    },
    setPageContent(state, content) {
      state.pageContent = content
    }
  }
})