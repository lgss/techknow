import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/pages/Home'
import Assess from '@/pages/Assess'

const fields = require('../../static/assess.json');
const answers =[];

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/assess',
      name: 'Assessment',
      component: Assess,
      props: {
        fields,
        answers
      }
    }
  ]
})
