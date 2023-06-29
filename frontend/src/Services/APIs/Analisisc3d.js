import axios from 'axios';

const instance = axios.create(
    {
        baseURL: 'http://3.131.153.81:9000/',
        timeout : 15000,
        headers: {
            'Content-Type': 'application/json',
        }
    }
);

export const analisisc3d = async (value) => {
    const {data} = await instance.post('/analisisc3d', {entrada: value});
    return data;
}
