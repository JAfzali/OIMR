<template>
  <v-card>
    <v-card-title>
      Orders
      <v-spacer></v-spacer>
      <v-card class="text-center">
        <v-dialog v-model="dialog" width="300">
          <v-card>
            <v-list-item two-line class="light-blue lighten-4">
              <v-list-item-content>
                <v-list-item-title class="headline"></v-list-item-title>
                <v-list-item-subtitle>Order Number</v-list-item-subtitle>
                <v-list-item-title class="headline">{{
                  currentOrdernr
                }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-divider></v-divider>
            <v-row align="center" justify="space-around">
              <v-btn
                :loading="recpdfload"
                depressed
                color="white"
                block
                @click="getReceivedPDF"
              >
                Receive
              </v-btn>
              <v-btn
                :loading="orderpdfload"
                depressed
                color="white"
                block
                @click="getOrderPDF"
              >
                Order Confirmation
              </v-btn>
              <v-btn depressed color="white" block @click="getCOC_MC">
                COC Machining
              </v-btn>
              <v-btn depressed color="white" block @click="getCOC_HB">
                COC Hardbanding
              </v-btn>
              <v-btn
                :loading="preinvpdfload"
                depressed
                color="white"
                block
                @click="getPreinvPDF"
              >
                Pre Invoice
              </v-btn>
              <v-btn
                :loading="insprepload"
                depressed
                color="white"
                block
                @click="getInspRepPDF"
              >
                Inspection Report
              </v-btn>
            </v-row>
          </v-card>
        </v-dialog>
      </v-card>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search (Order nr, PO, Item Number etc..)"
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-container fluid
      ><v-checkbox
        v-model="selected"
        label="Completed"
        value="completed"
      ></v-checkbox>
      <v-checkbox
        v-model="selected"
        label="Ongoing"
        value="ongoing"
      ></v-checkbox
    ></v-container>
    <v-data-table
      :loading="loading"
      :headers="headers"
      :items="filteredOrders"
      :search="search"
    >
      <template v-slot:item.action="{ item }">
        <v-btn dark x-small text color="black" @click="getPDF(item)">
          <v-icon>description</v-icon>
        </v-btn>
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import { mapGetters } from "vuex";
import axios from "axios";
export default {
  name: "orderconfirm",
  data() {
    return {
      selected: ["completed", "ongoing"],
      insprepload: false,
      preinvpdfload: false,
      recpdfload: false,
      currentrec: "",
      currentOrdernr: "",
      currentCOCHB: "",
      currentCOMC: "",
      dialog: false,
      loading: false,
      orderpdfload: false,
      search: "",
      headers: [
        {
          text: "Ord",
          align: "start",
          sortable: true,
          value: "Order_No"
        },
        { text: "Return Date", value: "Return_Date" },
        { text: "Completed", value: "Completed" },
        { text: "Ref", value: "Ref" },
        { text: "Item No", value: "Item_No" },
        { text: "Equipment", value: "Equipment" },
        { text: "Weight", value: "Weight" },
        { text: "Grade", value: "Grade" },
        { text: "Connection", value: "Connection_Rec" },
        { text: "Inspection", value: "Inspection_Spec" },
        { text: "Scope Of Work", value: "Scope_Of_Work" },
        { text: "QTY", value: "QTY_Recived" },
        { text: "PDF", value: "action", sortable: false }
      ],
      desserts: []
    };
  },
  computed: {
    ...mapGetters(["getUsername"]),
    filteredOrders() {
      if (this.selected.length == 2) {
        return this.desserts;
      } else if (this.selected == "completed") {
        return this.desserts.filter(order => {
          return order.Completed === "Yes";
        });
      } else if (this.selected == "ongoing") {
        return this.desserts.filter(order => {
          return order.Completed === "No";
        });
      }
    }
  },
  mounted() {
    this.loading = true;
    axios
      .get("/getOrderconfirm", {
        params: { username: this.$store.getters.getUsername }
      })
      .then(response => {
        console.log(response);
        this.desserts = response.data;
        this.loading = false;
      });
  },
  methods: {
    getPDF(item) {
      this.dialog = true;
      this.currentCOCHB = item.COC_Hardbanding;
      this.currentCOCMC = item.COC_Machining;
      this.currentOrdernr = item.Order_No;
      this.currentrec = item.Receive_No;
    },
    getReceivedPDF() {
      console.log(this.currentrec);
      this.recpdfload = true;
      axios
        .get("/getReceivedPDF", {
          params: { receivednr: this.currentrec }
        })
        .then(response => {
          this.recpdfload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    getCOC_HB() {
      window.open(this.currentCOCHB, "_blank");
    },
    getCOC_MC() {
      window.open(this.currentCOCMC, "_blank");
    },
    getOrderPDF() {
      console.log(this.currentOrdernr);
      this.orderpdfload = true;
      axios
        .get("/getOrderPDF", {
          params: { orderno: this.currentOrdernr }
        })
        .then(response => {
          this.orderpdfload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    getPreinvPDF() {
      console.log(this.currentOrdernr);
      this.preinvpdfload = true;
      axios
        .get("/getPreinvPDF", {
          params: { orderno: this.currentOrdernr }
        })
        .then(response => {
          this.preinvpdfload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    getInspRepPDF() {
      console.log(this.currentOrdernr);
      this.insprepload = true;
      axios
        .get("/getdpPDF", {
          params: { orderno: this.currentOrdernr }
        })
        .then(response => {
          this.insprepload = false;
          window.open(response.data.pdflink, "_blank");
        });
    }
  }
};
</script>

<style>
</style>
