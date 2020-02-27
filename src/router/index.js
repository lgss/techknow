import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/pages/Home'
import Assess from '@/pages/Assess'
import Result from '@/pages/Result'

const fields = require('../../static/assess.json');

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
        fields
      }
    },
    {
      path: '/result',
      name: 'Result',
      component: Result,
      props: true
    }
  ]
})
