import "whatwg-fetch";
import Vue from 'vue'
import App from './App'
import router from './router'
import vuetify from './plugins/vuetify';
import VueGtag from "vue-gtag";
import store from './store'

Vue.config.productionTip = false

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')

if (process.env.VUE_APP_GOOGLE_ANALYTICS_ID) {
  Vue.use(VueGtag, {
    config: { id: process.env.VUE_APP_GOOGLE_ANALYTICS_ID },
    appName: "rekommend",
    pageTrackerScreenviewEnabled: true,
    onReady: (gtag) => {
      const doTrack = Object.prototype.hasOwnProperty.call(localStorage, "ga_consent") && localStorage.ga_consent==="true"

      gtag('set', 'allowAdFeatures', doTrack)
      gtag('set', 'anonymizeIp', !doTrack)
    },
    enabled: !Object.prototype.hasOwnProperty.call(localStorage, "ga_consent") || localStorage.ga_consent==="true",
  }, router);
}