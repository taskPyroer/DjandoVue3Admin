<template>
  <el-container class="layout-container">
    <Aside />
    <el-container class="flex-center" :class="{ 'layout-backtop': !isFixedHeader }">
      <Header v-if="isFixedHeader" />
      <el-scrollbar
        ref="layoutDefaultsScrollbarRef"
        :class="{ 'layout-backtop': isFixedHeader }"
      >
        <Header v-if="!isFixedHeader" />
        <Main />
      </el-scrollbar>
    </el-container>
    <el-backtop target=".layout-backtop .el-scrollbar__wrap"></el-backtop>
  </el-container>
</template>

<script lang="ts">
import { computed, getCurrentInstance, watch,ref } from "vue";
import { useRoute } from "vue-router";
import { useThemeConfigStateStore } from "@/stores/themeConfig";
import Aside from "@/layout/component/aside.vue";
import Header from "@/layout/component/header.vue";
import Main from "@/layout/component/main.vue";
export default {
  name: "layoutDefaults",
  components: { Aside, Header, Main },
  setup() {
    const { proxy } = getCurrentInstance() as any;
    const route = useRoute();
    const theme = useThemeConfigStateStore();

    const layoutDefaultsScrollbarRef = ref()
    const isFixedHeader = computed(() => {
      return theme.themeConfig.isFixedHeader;
    });
    // 监听路由的变化
    watch(
      () => route.path,
      () => {
        proxy.$refs.layoutDefaultsScrollbarRef.wrapRef.scrollTop = 0;
        //proxy.$refs.layoutDefaultsScrollbarRef.setScrollTop(0)
      }
    );
    return {
      isFixedHeader,
    };
  },
};
</script>
