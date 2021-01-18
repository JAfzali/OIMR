<template>
  <v-container fluid>
    <pdf_menu :dialog="dialog" :currentOrdernr="currentOrdernr" :currentrec="currentrec" :currentCOCHB="currentCOCHB" :currentCOCMC="currentCOCMC"></pdf_menu>
    <!-- Stack the columns on mobile by making one full-width and the other half-width -->
    <v-row class="white">
      <v-col cols="1" md="12">
        <v-card class="white" elevation="0" tile>
          <v-row align="center" class="lightbox black--text pa-0 fill-height">
          </v-row>
          <v-row  align="center" class="lightbox black--text pa- fill-height">
            <v-col>
              <div style="color: #204060" class="display-1">
                <b>{{ getUsername }}</b>
              </div>
              <div style="color: #204060" class="display-0">{{ getAsset }}</div>
            </v-col>
          </v-row>
          <v-divider class="mx-0" color="white"></v-divider>
        </v-card>
      </v-col>
    </v-row>
    <!-- Columns are always 50% wide, on mobile and desktop -->
    <v-row class="white">
      <v-col cols="6">
        <v-card class="pa-10" outlined tile>
          <v-card to="/orderconfirm"  elevation="0">
          <h2>Orders</h2>
          </v-card>
          <br />
          <v-data-table
            height="250"
            :loading="commonload"
            :headers="header_order"
            :items="filterOrders"
            :items-per-page="5"
            class="elevation-1"
          >
            <template v-slot:item.action="{ item }">
              <v-btn dark x-small text color="black" @click="getPDF(item)">
                <v-icon>description</v-icon>
              </v-btn>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
      <v-col cols="6">
        <v-card class="pa-10" outlined tile>
          <h2>Inspection</h2>
          <br />
          <v-data-table
            height="250"
            :loading="commonload"
            :headers="header1"
            :items="filterInspection"
            :items-per-page="5"
            class="elevation-1"
          >
            <template v-slot:item.action="{ item }">
              <v-btn dark x-small text color="black" @click="getdpPDF(item)">
                <v-icon>description</v-icon>
              </v-btn>
            </template>
            <template v-slot:item.action1="{ item }">
              <v-btn dark x-small text color="black" @click="getExcel(item)">
                <v-icon>mdi-file-excel</v-icon>
              </v-btn>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
      <v-col cols="6">
        <v-card class="pa-10" outlined tile>
          <h2>Machining</h2>
          <br />
          <v-data-table
            height="250"
            :loading="commonload"
            :headers="header2"
            :items="filterMachining"
            :items-per-page="5"
            class="elevation-1"
          ></v-data-table>
        </v-card>
      </v-col>
      <v-col cols="6">
        <v-card class="pa-10" outlined tile>
          <h2>Hardbanding</h2>
          <br />
          <v-data-table
            :loading="commonload"
            height="250"
            :headers="header2"
            :items="filterHardbanding"
            :items-per-page="5"
            class="elevation-1"
          ></v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import axios from "axios";
import pdf_menu from '@/components/order_pdf_menu.vue'
export default {
  name: "completedorders",
  components: { pdf_menu },
  props: {
    source: String
  },
  data() {
    return {
      commonload: false,
      header1: [
        {
          text: "Order nr",
          align: "start",
          sortable: true,
          value: "Order_No"
        },
        { text: "Inspection date", value: "Return_Date" },
        { text: "Item no", value: "Item_No" },
        { text: "Equipment", value: "Equipment" },
        { text: "Qty", value: "QTY_Recived" },
        { text: "PDF", value: "action", sortable: false },
        { text: "Excel", value: "action1", sortable: false }
      ],
      header_order: [
        {
          text: "Order nr",
          align: "start",
          sortable: true,
          value: "Order_No"
        },
        { text: "Inspection date", value: "Return_Date" },
        { text: "Item no", value: "Item_No" },
        { text: "Equipment", value: "Equipment" },
        { text: "Qty", value: "QTY_Recived" },
        { text: "PDF", value: "action", sortable: false }
      ],
      header2: [
        {
          text: "Order nr",
          align: "start",
          sortable: true,
          value: "Order_No"
        },
        { text: "Inspection date", value: "Return_Date" },
        { text: "Item no", value: "Item_No" },
        { text: "Equipment", value: "Equipment" },
        { text: "Qty", value: "QTY_Recived" },
        { text: "Excel", value: "action1", sortable: false }
      ],
      orders: [],
      insp: [
        {
          name: "10404",
          calories: "02/10/2020",
          fat: "Saipem",
          carbs: "SC8800DC.01",
          protein: "Drill Collar",
          iron: "3"
        },
        {
          name: "10403",
          calories: "02/10/2020",
          fat: "Saipem",
          carbs: "SC8434DC.01",
          protein: "Drill Collar",
          iron: "1"
        },
        {
          name: "10402",
          calories: "02/10/2020",
          fat: "Saipem",
          carbs: "SC8512DP.01",
          protein: "Drill Pipe",
          iron: "1"
        },
        {
          name: "10254",
          calories: "24/06/2020",
          fat: "Saipem",
          carbs: "SC8800DC.01",
          protein: "Drill Collar",
          iron: "124"
        }
      ],
      mach: [],
      hard: [],
      currentrec: "",
      currentOrdernr: "",
      currentCOCHB: "",
      currentCOCMC: "",
      dialog: false
    };
  },
  methods: {
    getdpPDF(item) {
      console.log(item.Order_No);
      this.commonload = true;
      axios
        .get("/getdpPDF", {
          params: { orderno: item.Order_No }
        })
        .then(response => {
          this.commonload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    getExcel(item) {
      console.log(item.Order_No);
      this.commonload = true;
      axios
        .get("/getdpExcel", {
          params: { orderno: item.Order_No }
        })
        .then(response => {
          this.commonload = false;
          window.open(response.data.excellink, "_blank");
        });
    },
    getOrderPDF(item) {
      console.log(item.Order_No);
      this.commonload = true;
      axios
        .get("/getOrderPDF", {
          params: { orderno: item.Order_No }
        })
        .then(response => {
          this.commonload = false;
          window.open(response.data.pdflink, "_blank");
        });
    },
    getPDF(item) {
      this.dialog = true;
      this.currentCOCHB = item.COC_Hardbanding;
      this.currentCOCMC = item.COC_Machining;
      this.currentOrdernr = item.Order_No;
      this.currentrec = item.Receive_No;
    }
  },
  mounted() {
    this.commonload = true;
    axios
      .get("/getOrderconfirm", {
        params: { username: this.$store.getters.getUsername }
      })
      .then(response => {
        console.log(response);
        this.orders = response.data;
        this.commonload = false;
      });
  },
  computed: {
    ...mapGetters(["getEmail", "getUsername", "getAssetlist", "getAsset"]),
    isAssetList() {
      if (this.getAssetlist.length > 0) {
        return true;
      } else {
        return false;
      }
    },
    filterOrders() {
      return this.orders.filter(order => {
        return order.Completed === "Yes";
      });
    },
    filterInspection() {
      return this.orders.filter(order => {
        return order.Check_Inspection === "Yes";
      });
    },
    filterMachining() {
      return this.orders.filter(order => {
        return order.Check_Machining === "Yes";
      });
    },
    filterHardbanding() {
      return this.orders.filter(order => {
        return order.Check_Hardbanding === "Yes";
      });
    }
  }
};
</script>

<style lang="css" scoped>
.inline {
  display: inline-block;
  margin-right: 10px;
}
</style>
