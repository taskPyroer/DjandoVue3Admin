<template>
	<div class="layout-navbars-breadcrumb-user-news">
		<div class="head-box">
			<div class="head-box-title">{{ $t('message.user.newTitle') }}</div>
			<div class="head-box-btn" v-if="newsList.length > 0" @click="onAllReadClick">{{ $t('message.user.newBtn') }}</div>
		</div>
		<div class="content-box">
			<template v-if="newsList.length > 0">
				<div class="content-box-item" v-for="(v, k) in newsList" :key="k">
					<div>{{ v.title }}</div>

					<div class="content-box-time">发布时间：{{ dateStrFormat(v.create_datetime) }}</div>
				</div>
			</template>
			<el-empty :description="$t('message.user.newDesc')" v-else></el-empty>
		</div>
		<div class="foot-box" @click="onGoToGiteeClick" v-if="newsList.length > 0">{{ $t('message.user.newGo') }}</div>
	</div>
</template>

<script lang="ts">
import { reactive, toRefs,onMounted, } from 'vue';
import {listReceiveNotice} from "@/api/system/notice";
import {useRouter} from "vue-router";
export default {
	name: 'layoutBreadcrumbUserNews',
	setup() {
		const router = useRouter();
		const state = reactive({
			newsList: [],
		});
		const handleQuery = () => {
      listReceiveNotice({pageNum: 1,pageSize: 3}).then((response) => {
						state.newsList = response.data.data;
					}
			);
		};
		// 全部已读点击
		const onAllReadClick = () => {
			state.newsList = [];
		};
		// 前往通知中心点击
		const onGoToGiteeClick = () => {
			router.push("/system/message-center")
		};
		onMounted(() => {
			handleQuery()
		})
		return {
			onAllReadClick,
			onGoToGiteeClick,
			...toRefs(state),
		};
	},
};
</script>

<style scoped lang="scss">
.layout-navbars-breadcrumb-user-news {
	.head-box {
		display: flex;
		border-bottom: 1px solid #ebeef5;
		box-sizing: border-box;
		color: #333333;
		justify-content: space-between;
		height: 35px;
		align-items: center;
		.head-box-btn {
			color: var(--color-primary);
			font-size: 13px;
			cursor: pointer;
			opacity: 0.8;
			&:hover {
				opacity: 1;
			}
		}
	}
	.content-box {
		font-size: 13px;
		.content-box-item {
			padding-top: 12px;
			&:last-of-type {
				padding-bottom: 12px;
			}
			.content-box-msg {
				color: #999999;
				margin-top: 5px;
				margin-bottom: 5px;
			}
			.content-box-time {
				color: #999999;
			}
		}
	}
	.foot-box {
		height: 35px;
		color: var(--color-primary);
		font-size: 13px;
		cursor: pointer;
		opacity: 0.8;
		display: flex;
		align-items: center;
		justify-content: center;
		border-top: 1px solid #ebeef5;
		&:hover {
			opacity: 1;
		}
	}
	::v-deep(.el-empty__description p) {
		font-size: 13px;
	}
}
</style>
