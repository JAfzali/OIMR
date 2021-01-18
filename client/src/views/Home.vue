<template>
  <v-container>
    <!-- Stack the columns on mobile by making one full-width and the other half-width -->
    <v-row class="white">
      <v-col cols="1" md="12">
        <v-card class="white" elevation="0" tile>
          <v-row align="center" class="lightbox black--text pa-0 fill-height">
          </v-row>
          <v-row align="center" class="lightbox black--text pa- fill-height">
            <v-col>
              <div style="color: #204060" class="display-1">
                <b>{{ getUsername }}</b>
              </div>
              <div
                v-if="isAssetList"
                style="color: #204060; width: 20%; margin: 0 auto;"
                class="display-1"
              >
                <v-select
                  v-if="isAssetList"
                  :placeholder="[[currentAsset]]"
                  v-model="select"
                  :items="filteredAssets"
                  label=""
                  persistent-hint
                  return-object
                  single-line
                  dense
                ></v-select>
              </div>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <!-- Columns are always 50% wide, on mobile and desktop -->
    <v-row class="white">
      <v-col v-for="card in cards1" :key="card" cols="6">
        <v-card
          :to="card.path"
          class="pa-10"
          outlined
          tile
          dark
          :style="{
            'background-color': `rgb(${card.color.red}, ${card.color.green}, ${card.color.blue})`
          }"
        >
          <h2>{{ card.name }}</h2>
          <br />
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "Home",
  props: {
    source: String
  },
  data() {
    return {
      select: "Florida",
      ites: [
        { state: "Florida" },
        { state: "Georgia" },
        { state: "Nebraska" },
        { state: "California" },
        { state: "New York" }
      ],
      ite: ["Florida", "Georgia", "Nebraska", "California", "New York"],
      drawer: false,
      cards1: [
        {
          name: "Inventory",
          color: {
            red: "32",
            green: "64",
            blue: "96"
          },
          path: "/inventory"
        },
        {
          name: "Shipping",
          color: {
            red: "66",
            green: "165",
            blue: "245"
          },
          path: "/delivery"
        },
        {
          name: "Ongoing Orders",
          color: {
            red: "189",
            green: "189",
            blue: "189"
          },
          path: "ongoingorders"
        },
        {
          name: "Completed Orders",
          color: {
            red: "38",
            green: "198",
            blue: "218"
          },
          path: "completedorders"
        }
      ]
    };
  },
  watch: {
    select: function() {
      if (this.select === "Fleet Inventory") {
        this.setasset({ asset: this.select });
        this.setfleet({ fleet: true });
      } else {
        this.setasset({ asset: this.select });
        this.setfleet({ fleet: false });
      }
    }
  },
  methods: {
    ...mapActions(["setasset", "setfleet"])
  },
  mounted() {
    if(this.isAssetList === true) {
        this.items = this.getAssetlist.push("Fleet Inventory");
    } else {
      this.items = this.getAssetlist;
    }
    
  },
  computed: {
    ...mapGetters(["getEmail", "getUsername", "getAsset", "getAssetlist"]),
    isAssetList() {
      if (this.getAssetlist.length > 0) {
        return true;
      } else {
        return false;
      }
    },
    filteredAssets() {
      return this.getAssetlist.filter(item => {
        return item != this.getAsset;
      });
    },
    currentAsset() {
      return this.getAsset;
    }
  }
};
</script>

<style lang="css" scoped>
input {
  float: left;
}
</style>
