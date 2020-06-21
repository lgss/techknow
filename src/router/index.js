import Vue from "vue";
import Router from "vue-router";

import Home from "@/pages/Home";
import Assess from "@/pages/Assess";
import Result from "@/pages/Result";
import Select from "@/pages/Select";

Vue.use(Router);

export default new Router({
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
            path: "/result",
            name: "Result",
            component: Result,
            props: true,
            meta: {
                title: "Resources for you",
            },
        },
    ],
});
