import { getHttp } from "../utils/request";
export const getSourceList = (params) => getHttp("/getSourceList", params);
export const getAllWords = (params) => getHttp("/getAllWords", params);
