<template>
    <v-input v-model="sel" :rules="rules">
        <v-container max-width="1200" class="mx-auto">
            <div class="d-flex flex-wrap align-center">
                <div class="text-left">
                    <label ref="label" role="heading" aria-level="3" class="text-h3 mb-2" v-text="title" tabindex="0"></label>
                    <div class="font-weight-bold mb-0" v-text="subtitle" tabindex="0"></div>
                </div>
                <v-spacer></v-spacer>
                <v-avatar class="ma-3" size="125" tile>
                    <v-icon size="80">mdi-comment-question-outline</v-icon>
                </v-avatar>
            </div>
            <v-item-group multiple v-model="sel">
                <v-row dense>
                    <v-col v-for="(item, i) in items" :key="i" cols="12">
                        <choice
                            :value="item"
                            :index="i"
                            :label="item[itemLabelKey]"
                            :imgSrc="item[itemImgSrcKey]"
                            :imgAlt="item[itemImgAltKey]"
                        />
                    </v-col>
                </v-row>
            </v-item-group>
        </v-container>
    </v-input>
</template>

<script>
import Choice from "./controls/Choice";

export default {
    name: "item",
    components: {
        choice: Choice,
    },
    props: [
        "title",
        "subtitle",
        "items",
        "itemLabelKey",
        "itemImgSrcKey",
        "itemImgAltKey",
        "type",
    ],
    data() {
        return {
            rules: [
                (val) =>
                    !!val.length ||
                    `Please select at least one ${this.type || "option"}.`,
            ],
        };
    },
    methods: {
        focus() {
            console.log("attempting to focus on item")
            this.$refs.label.focus();
        }
    },
    computed: {
        sel:{
            get: function() {
                return this.items.filter(item => item.selected);
            },
            set: function() {
            }
        },

    }
};
</script>
