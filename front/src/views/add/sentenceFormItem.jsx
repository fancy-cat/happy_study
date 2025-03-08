import {Form, Input } from 'antd';
import DebounceSelect from '../../components/debounceSelect.jsx';
const { TextArea } = Input;

export default function ToneFormItems() {
  return <>
    <Form.Item label="句子" name="sentence">
      <TextArea rows={1} placeholder="请输入"/>
    </Form.Item>
    <Form.Item label="翻译" name="translate">
      <TextArea rows={1} placeholder="请输入"/>
    </Form.Item>
    <Form.Item label="单词" name="words">
      <DebounceSelect
        mode="multiple"
        placeholder="请选择"
        fetchType={'下拉求值类型'}
        style={{
          width: '100%',
        }}
        onChange={(newValue) => {
          console.log(newValue)
        }}
      />
    </Form.Item>
    <Form.Item label="备注" name="remark">
      <TextArea rows={4} placeholder="请输入"/>
    </Form.Item>
  </>
}