<template>
  <div id="inspire">
    <v-navigation-drawer v-model="drawer" app temporary color="white">
      <v-layout justify-space-between column fill-height>
        <v-flex>
          <v-list>
            <v-list-item two-line>
              <v-list-item-avatar color="#377AC8">
                <v-icon>mdi-account-circle</v-icon>
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-title
                  ><b>{{ getUsername }}</b></v-list-item-title
                >
                <v-list-item-subtitle>{{ getAsset }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
            <v-divider></v-divider>
            <router-link style="text-decoration: none" :to="{ name: test }">
              <v-list-item link>
                <v-list-item-action>
                  <v-icon color="#377AC8">mdi-home</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title class="text-left">Home</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </router-link>
            <v-divider></v-divider>
            <v-list-group
              v-for="rute in routes"
              :key="rute.name"
              :value="false"
            >
              <template v-slot:activator>
                <v-list-item-action>
                  <v-icon color="#377AC8">{{ rute.iconname }}</v-icon>
                </v-list-item-action>
                <v-list-item-title class="text-left">{{
                  rute.name
                }}</v-list-item-title>
              </template>

              <v-list-item
                v-for="element in rute.sublist"
                :key="element.subname"
                :to="{ name: element.route }"
                style="text-decoration: none"
              >
                <v-list-item-title class="text-left">{{
                  element.subname
                }}</v-list-item-title>
              </v-list-item>
            </v-list-group>
          </v-list>
        </v-flex>
      </v-layout>
    </v-navigation-drawer>
    <v-app-bar app color="white" flat hide-on-scroll>
      <v-app-bar-nav-icon
        @click.stop="drawer = !drawer"
        :disabled="isAssetPage"
      ></v-app-bar-nav-icon>
      <v-toolbar-title>{{ getroute() }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-img
        class="white--text align-end"
        height="50px"
        width="70px"
        contain
        :src="image"
      ></v-img>
      <v-spacer></v-spacer>
      <v-btn dark color="#204060" @click="logout">Log out</v-btn>
      <div></div>
    </v-app-bar>
  </div>
</template>

<script>
import firebase from "firebase";
import { mapActions, mapGetters } from "vuex";
import image from "../assets/picture.png";
export default {
  name: "navbar",
  data() {
    return {
      drawer: false,
      test: "Home",
      image: image,
      routes: [
        {
          route: "orderconf",
          iconname: "check_box",
          name: "Order Confirmation",
          sublist: [
            {
              subname: "Tubular",
              icon: "",
              route: "orderconfirm"
            },
            {
              subname: "BHA",
              icon: ""
            }
          ]
        },
        {
          route: "insp",
          iconname: "zoom_in",
          name: "Inspection",
          sublist: [
            {
              subname: "Tubular",
              icon: ""
            },
            {
              subname: "BHA",
              icon: ""
            }
          ]
        },
        {
          route: "inventory",
          iconname: "view_module",
          name: "Inventory",
          sublist: [
            {
              subname: "Inventory Overview",
              icon: "",
              route: "inventory"
            },
            {
              subname: "Received",
              icon: "",
              route: "received"
            },
            {
              subname: "Rack Location",
              icon: "",
              route: "racklocation"
            }
          ]
        },
        {
          route: "preinvoice",
          iconname: "description",
          name: "Pre Invoice",
          sublist: [
            {
              subname: "Tubular",
              icon: "",
              route: "preinvoice"
            },
            {
              subname: "BHA",
              icon: ""
            }
          ]
        },
        {
          route: "shipping",
          iconname: "local_shipping",
          name: "Shipping",
          sublist: [
            {
              subname: "Tubular",
              icon: "",
              route: "delivery"
            },
            {
              subname: "BHA",
              icon: ""
            }
          ]
        }
      ]
    };
  },
  methods: {
    ...mapActions(["logOut"]),
    logout: function() {
      firebase
        .auth()
        .signOut()
        .then(() => {
          this.logOut();
          this.$router.replace("login");
        });
    },
    getroute: function() {
      return this.$route.meta.displayname;
    }
  },
  computed: {
    ...mapGetters(["getUsername", "getAsset"]),
    isAssetPage() {
      if (this.$route.path === "/asset") {
        return true;
      } else {
        return false;
      }
    }
  }
};
</script>

<style lang="css" scoped>
</style>
