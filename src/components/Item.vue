<template>
    <v-input v-model="sel" :rules="rules">
        <v-container max-width="1200" class="mx-auto pt-0">
            <div class="d-flex flex-wrap">
                <v-row>
                    <v-col cols=auto class="align-self-center">
                        <v-icon class="ma-0" size="100">mdi-comment-question-outline</v-icon>
                    </v-col>
                    <v-col sm=9 md=9 lg=9>
                    <div class="text-left">
                        <label ref="label" role="heading" aria-level="3" class="text-h4 mb-2" tabindex="0">
                            {{title}}
                        </label>
                        <div class="text-h5 font-weight-bold mb-0" tabindex="0">
                            {{subtitle}}
                        </div>
                    </div>
                    </v-col>
                </v-row>
            </div>
            <v-item-group multiple v-model="sel">
                <v-row dense>
                    <v-col
                        class="flex-grow-0 flex-shrink-0 ie-flex"
                        v-for="(item, i) in display_items"
                        :key="i"
                    >
                        <choice
                            :value="item"
                            :index="i"
                            :label="item[itemLabelKey]"
                            :imgSrc="item.img.src"
                            :imgAlt="item.img.alt"
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
    props: ["title", "subtitle", "items", "type", "itemLabelKey"],
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
            console.log("attempting to focus on item");
            this.$refs.label.focus();
        },
    },
    computed: {
        display_items() {
            return this.items.map((x) => {
                x.img = x.img || {};
                return x;
            });
        },
        sel: {
            get: function() {
                return this.items.filter((item) => item.selected);
            },
            set: function() {},
        },
    },
};
</script>

<style scoped>
    .ie-flex
    {
        width: min-content;
        flex: 1 1 auto;
    }
</style>