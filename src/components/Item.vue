<template>
    <v-sheet max-width="1200" class="mx-auto">   
        <div class="d-flex flex-wrap align-center">
            <div class="text-left">
                <h2>{{title}}</h2>
                <h3>{{subtitle}}</h3>
            </div>
            <v-spacer></v-spacer>
            <v-avatar class="ma-3" size="125" tile>
                <v-icon size="80">mdi-comment-question-outline</v-icon>
            </v-avatar>
        </div>
        <v-item-group multiple model="sel">
            <v-row dense>
                <v-col v-for="(item, i) in items" :key="i" cols="12">
                    <choice :value="item" :index="i" :label="item[itemLabelKey]" :imgSrc="item[itemImgSrcKey]" :imgAlt="item[itemImgAltKey]"/>
                </v-col>
            </v-row>
        </v-item-group>
    </v-sheet>
</template>

<script>

import Choice from "./controls/Choice"

export default {
    name: "item",
    components: {
        "choice": Choice,
    },
    props: ["title","subtitle","items","itemLabelKey","itemImgSrcKey","itemImgAltKey"]
};
</script>
