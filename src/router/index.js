import Vue from "vue";
import Router from "vue-router";

import Home from '@/pages/Home'
import Assess from '@/pages/Assess'
import Result from '@/pages/Result'
import Select from '@/pages/Select'
import Terms from '@/pages/Terms'
import Accessibility from '@/pages/Accessibility'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: "/",
            name: "Home",
            component: Home,
            meta: {
                title: "Hello and Welcome",
            },
        },
        {
            path: "/select",
            name: "Select",
            component: Select,
            meta: {
                title: "Choose your journey",
            },
        },
        {
            path: "/assess",
            name: "Assessment",
            props: true,
            component: Assess,
            meta: {
                title: "Questions",
            },
        },
        {
            path: "/result/:id",
            name: "Result",
            component: Result,
            props: true,
            meta: {
                title: "Resources for you",
            },
        },
        {
            path: '/terms',
            name: 'terms',
            component: Terms,
            meta: {
                title: "Terms & Conditions"
            }
        },
        {
            path: '/accessibility',
            name: 'accessibility',
            component: Accessibility,
            meta: {
                title: "Accessibility statement"
            }
        }
    ],
});
