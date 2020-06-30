<template>
    <v-sheet max-width="1200" class="mx-auto">   
        <div class="text-left">
            <h1>{{title}}</h1>
            <h2>{{subtitle}}</h2>
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
