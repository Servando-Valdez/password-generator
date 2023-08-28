import {api} from "./axiosInstance"
import {ParamsPassword} from "../interfaces/interfaces";
import {Password} from "../interfaces/interfaces";

export class PasswordService{
    private readonly http = api;
    public async get(url: string, params: ParamsPassword): Promise<Password>{
        try {
            const response = await this.http.get<Password>(url, {params});
            return response.data;
        } catch (error) {
            throw error;
        }
    }
}