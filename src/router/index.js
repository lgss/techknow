import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/pages/Home'
import Assess from '@/pages/Assess'
import Result from '@/pages/Result'

const fields = require('../../static/assess.json');
const answers =[];

Vue.use(Router)

const results =  require('../../static/resource.json');

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
    },
    {
      path: '/result',
      name: 'Result',
      component: Result,
      props: {
          results,
          answers
      }
    }
  ]
})
